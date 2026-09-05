"""Assemble only public static assets after capture tests, never workspace secrets."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
site = ROOT / '_site'
site.mkdir(exist_ok=False)
shutil.copyfile(ROOT / 'site/index.html', site / 'index.html')
shutil.copyfile(ROOT / 'skills/web-rebuild/assets/reference.html', site / 'reference.html')
(site / 'previews').mkdir()
for width in [320,768,1440]:
    shutil.copyfile(ROOT / f'artifacts/reference-{width}.png', site / f'previews/reference-{width}.png')
(site / '.nojekyll').touch()
print('Static showcase assembled from an explicit public-file allowlist.')
