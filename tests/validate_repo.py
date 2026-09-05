"""Check the package contract and local Markdown targets, without network access."""
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/web-rebuild/SKILL.md'
text = SKILL.read_text(encoding='utf-8')
assert text.startswith('---\nname: web-rebuild\n'), 'Missing/mismatched frontmatter name'
assert len(text.splitlines()) < 500, 'Keep the entry point under 500 lines'
assert len(list((ROOT / 'skills').rglob('SKILL.md'))) == 1, 'Exactly one public skill is expected'
for relative in ['README.md', 'LICENSE', 'SECURITY.md', 'CONTRIBUTING.md', 'docs/README.id.md',
                 'skills/web-rebuild/assets/reference.html', 'skills/web-rebuild/scripts/compare_images.py']:
    assert (ROOT / relative).is_file(), f'Missing package file: {relative}'
for doc in ROOT.rglob('*.md'):
    if '.git' in doc.parts:
        continue
    for target in re.findall(r'\]\(([^\s)]+)\)', doc.read_text(encoding='utf-8')):
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        assert (doc.parent / unquote(parsed.path)).exists(), f'Broken local link in {doc}: {target}'
cases = json.loads((ROOT / 'evals/cases.json').read_text(encoding='utf-8'))
assert len(cases) == 10 and len({case['id'] for case in cases}) == 10
assert all(case['expect'] and case['fail'] for case in cases)
print('Package contract, local Markdown targets, and ten evaluation case definitions validated.')

for name in ['design-quality.md', 'stack-adapters.md']:
    assert f'references/{name}' in text, f'Unlinked core guide: {name}'
    assert (SKILL.parent / 'references' / name).is_file()
assert 'Do not introduce emoji' in text
assert 'Brief-led creation' in text
assert 'version: "0.2.0"' in text
print('v0.2 design policy, guide links, and entry-point metadata validated.')
