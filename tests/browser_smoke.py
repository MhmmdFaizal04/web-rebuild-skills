"""Synthetic capture/helper pipeline check, NOT a model reconstruction benchmark."""
import importlib.util
import json
from pathlib import Path
import platform

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('compare_images', ROOT / 'skills/web-rebuild/scripts/compare_images.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
output = ROOT / 'artifacts'
output.mkdir(exist_ok=False)
manifest = {'purpose': 'Synthetic fixture capture, not an AI rebuild', 'os': platform.platform(), 'captures': []}
with sync_playwright() as p:
    browser = p.chromium.launch()
    manifest['browser'] = browser.version
    for width, height in [(320, 900), (768, 1024), (1440, 1000)]:
        context = browser.new_context(viewport={'width': width, 'height': height}, device_scale_factor=1,
                                      locale='en-US', timezone_id='UTC', color_scheme='light', reduced_motion='reduce')
        page = context.new_page()
        errors = []
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.goto((ROOT / 'skills/web-rebuild/assets/reference.html').as_uri())
        page.evaluate('document.fonts.ready')
        assert page.title().startswith('Fieldnotes Studio')
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), f'Overflow at {width}'
        reference = output / f'reference-{width}.png'
        candidate = output / f'control-{width}.png'
        page.screenshot(path=str(reference), animations='disabled', scale='css')
        page.screenshot(path=str(candidate), animations='disabled', scale='css')
        assert module.compare(reference, candidate, output / f'control-diff-{width}')['passed']
        page.add_style_tag(content='h1 { color: #0044ff !important; }')
        mutated = output / f'mutated-{width}.png'
        page.screenshot(path=str(mutated), animations='disabled', scale='css')
        assert not module.compare(reference, mutated, output / f'mutation-diff-{width}')['passed']
        summary = page.locator('summary')
        summary.focus()
        page.keyboard.press('Enter')
        assert page.locator('details').evaluate('(node) => node.open')
        page.keyboard.press('Enter')
        assert not page.locator('details').evaluate('(node) => node.open')
        assert not errors, errors
        manifest['captures'].append({'width': width, 'height': height, 'dpr': 1, 'scale': 'css',
                                     'locale': 'en-US', 'timezone': 'UTC', 'reduced_motion': 'reduce',
                                     'reference': reference.name, 'control': candidate.name, 'mutated': mutated.name})
        context.close()
    browser.close()
(output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
print('Three viewport captures, identical controls, altered-image detection, overflow and disclosure checks passed.')
