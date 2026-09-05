import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from PIL import Image

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/web-rebuild/scripts/compare_images.py'
spec = importlib.util.spec_from_file_location('compare_images', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class CompareTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.left, self.right = self.root / 'left.png', self.root / 'right.png'
        Image.new('RGB', (2, 2), 'white').save(self.left)
        Image.new('RGB', (2, 2), 'white').save(self.right)
        self.output = self.root / 'output'

    def test_identical_outputs_and_hashes(self):
        report = module.compare(self.left, self.right, self.output)
        self.assertTrue(report['passed'])
        self.assertEqual(report['different_pixels'], 0)
        self.assertEqual(report['reference_sha256'], report['candidate_sha256'])
        self.assertEqual(json.loads((self.output / 'report.json').read_text()), report)
        with Image.open(self.output / 'side-by-side.png') as image:
            self.assertEqual(image.size, (4, 2))
        self.assertTrue((self.output / 'overlay.png').is_file())
        self.assertTrue((self.output / 'difference.png').is_file())

    def test_one_changed_pixel_and_ratio_boundary(self):
        image = Image.new('RGB', (2, 2), 'white')
        image.putpixel((0, 0), (235, 255, 255))
        image.save(self.right)
        report = module.compare(self.left, self.right, self.output, 19, 0.25)
        self.assertEqual(report['different_pixels'], 1)
        self.assertEqual(report['mismatch_ratio'], 0.25)
        self.assertTrue(report['passed'])
        self.assertFalse(module.compare(self.left, self.right, self.root / 'strict', 19, 0.24)['passed'])
        self.assertEqual(module.compare(self.left, self.right, self.root / 'boundary', 20)['different_pixels'], 0)

    def test_transparency_composited_on_white(self):
        Image.new('RGBA', (2, 2), (0, 0, 0, 0)).save(self.right)
        self.assertTrue(module.compare(self.left, self.right, self.output)['passed'])

    def test_dimensions_rejected_without_output(self):
        Image.new('RGB', (3, 2)).save(self.right)
        with self.assertRaisesRegex(ValueError, 'dimensions differ'):
            module.compare(self.left, self.right, self.output)
        self.assertFalse(self.output.exists())

    def test_invalid_parameters(self):
        for threshold in [-1, 256, 1.5, True]:
            with self.subTest(threshold=threshold), self.assertRaises(ValueError):
                module.compare(self.left, self.right, self.output, threshold)
        for ratio in [-0.1, 1.1, float('nan'), float('inf')]:
            with self.subTest(ratio=ratio), self.assertRaises(ValueError):
                module.compare(self.left, self.right, self.output, 0, ratio)
        self.assertFalse(self.output.exists())

    def test_existing_output_preserved(self):
        self.output.mkdir()
        sentinel = self.output / 'keep.txt'
        sentinel.write_text('keep')
        with self.assertRaises(FileExistsError):
            module.compare(self.left, self.right, self.output)
        self.assertEqual(sentinel.read_text(), 'keep')

    def test_non_png_and_corrupt_input_rejected(self):
        Image.new('RGB', (2, 2)).save(self.right, format='JPEG')
        with self.assertRaises(ValueError):
            module.compare(self.left, self.right, self.output)
        self.right.write_bytes(b'not an image')
        with self.assertRaises(OSError):
            module.compare(self.left, self.right, self.output)

    def test_oversized_input_rejected(self):
        old = module.MAX_PIXELS
        module.MAX_PIXELS = 3
        try:
            with self.assertRaisesRegex(ValueError, 'exceeds'):
                module.compare(self.left, self.right, self.output)
        finally:
            module.MAX_PIXELS = old

    def test_animated_png_rejected(self):
        first = Image.new('RGB', (2, 2), 'red')
        first.save(self.right, save_all=True, append_images=[Image.new('RGB', (2, 2), 'blue')], duration=100, loop=0)
        with self.assertRaisesRegex(ValueError, 'single-frame'):
            module.compare(self.left, self.right, self.output)

    def test_16_bit_grayscale_rejected(self):
        for value in (256, 65535):
            Image.new('I;16', (2, 2), value).save(self.right)
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, '16-bit'):
                module.compare(self.left, self.right, self.output)

    def test_encoded_size_limit(self):
        with patch.object(module, 'MAX_BYTES', 4), self.assertRaisesRegex(ValueError, 'encoded bytes'):
            module.compare(self.left, self.right, self.output)

    def test_hash_matches_decoded_bytes_after_path_replacement(self):
        original_hash = hashlib.sha256(self.right.read_bytes()).hexdigest()
        original_load = module.load_png

        def replace_after_decode(path):
            result = original_load(path)
            if path == self.right:
                Image.new('RGB', (2, 2), 'black').save(self.right)
            return result

        with patch.object(module, 'load_png', side_effect=replace_after_decode):
            report = module.compare(self.left, self.right, self.output)
        self.assertTrue(report['passed'])
        self.assertEqual(report['candidate_sha256'], original_hash)
        self.assertNotEqual(report['candidate_sha256'], hashlib.sha256(self.right.read_bytes()).hexdigest())

    def test_cli_exit_codes(self):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(module.main([str(self.left), str(self.right), '--output', str(self.output)]), 0)
            Image.new('RGB', (2, 2), 'black').save(self.right)
            self.assertEqual(module.main([str(self.left), str(self.right), '--output', str(self.root / 'fail')]), 1)
            self.assertEqual(module.main([str(self.left), str(self.root / 'missing'), '--output', str(self.root / 'bad')]), 2)


if __name__ == '__main__':
    unittest.main()
