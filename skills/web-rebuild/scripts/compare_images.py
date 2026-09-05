"""Compare local PNG captures without resizing, networking, or replacing evidence."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import sys
import warnings

from PIL import Image, ImageChops, ImageStat

MAX_PIXELS = 4_000_000


def load_png(path):
    with warnings.catch_warnings():
        warnings.simplefilter('error', Image.DecompressionBombWarning)
        with Image.open(path) as image:
            if image.format != 'PNG' or getattr(image, 'n_frames', 1) != 1:
                raise ValueError('Only single-frame PNG images are supported')
            if image.width * image.height > MAX_PIXELS:
                raise ValueError(f'Image exceeds {MAX_PIXELS} pixels; use a viewport capture')
            image.load()
            rgba = image.convert('RGBA')
            return Image.alpha_composite(Image.new('RGBA', rgba.size, 'white'), rgba).convert('RGB')


def compare(reference, candidate, output, threshold=0, max_mismatch_ratio=0.0):
    if type(threshold) is not int or not 0 <= threshold <= 255:
        raise ValueError('threshold must be an integer from 0 to 255')
    if not math.isfinite(max_mismatch_ratio) or not 0 <= max_mismatch_ratio <= 1:
        raise ValueError('max-mismatch-ratio must be finite and between 0 and 1')
    reference, candidate, output = Path(reference), Path(candidate), Path(output)
    left, right = load_png(reference), load_png(candidate)
    if left.size != right.size:
        raise ValueError(f'Image dimensions differ: {left.size} versus {right.size}; do not resize evidence')
    difference = ImageChops.difference(left, right)
    channels = difference.split()
    maximum = ImageChops.lighter(ImageChops.lighter(channels[0], channels[1]), channels[2])
    histogram = maximum.histogram()
    different = sum(histogram[threshold + 1:])
    pixels = left.width * left.height
    ratio = different / pixels
    with reference.open('rb') as source, candidate.open('rb') as rebuilt:
        reference_hash = hashlib.file_digest(source, 'sha256').hexdigest()
        candidate_hash = hashlib.file_digest(rebuilt, 'sha256').hexdigest()
    report = {
        'schema_version': 1,
        'reference': str(reference),
        'candidate': str(candidate),
        'reference_sha256': reference_hash,
        'candidate_sha256': candidate_hash,
        'width': left.width, 'height': left.height,
        'threshold': threshold, 'max_mismatch_ratio': max_mismatch_ratio,
        'different_pixels': different, 'total_pixels': pixels, 'mismatch_ratio': ratio,
        'mean_absolute_channel_error': sum(ImageStat.Stat(difference).mean) / 3,
        'passed': ratio <= max_mismatch_ratio,
        'note': 'Image tolerance only; not a usability, accessibility, or model-quality score.',
    }
    output.mkdir(parents=True, exist_ok=False)
    side = Image.new('RGB', (left.width * 2, left.height))
    side.paste(left, (0, 0))
    side.paste(right, (left.width, 0))
    side.save(output / 'side-by-side.png')
    Image.blend(left, right, 0.5).save(output / 'overlay.png')
    difference.save(output / 'difference.png')
    (output / 'report.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('reference', type=Path)
    parser.add_argument('candidate', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--threshold', type=int, default=0)
    parser.add_argument('--max-mismatch-ratio', type=float, default=0.0)
    args = parser.parse_args(argv)
    try:
        report = compare(args.reference, args.candidate, args.output, args.threshold, args.max_mismatch_ratio)
    except (OSError, ValueError, Image.DecompressionBombError, Image.DecompressionBombWarning) as error:
        print(f'Comparison failed: {error}', file=sys.stderr)
        return 2
    print(json.dumps(report, indent=2))
    return 0 if report['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
