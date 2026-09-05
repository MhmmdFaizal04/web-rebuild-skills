"""HTTP URL inspection and capture controls; never an AI reconstruction benchmark."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import importlib.util
import json
import os
from pathlib import Path
import platform
from threading import Thread

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = 'https://mhmmdfaizal04.github.io/web-rebuild-skills/reference.html'
spec = importlib.util.spec_from_file_location('compare_images', ROOT / 'skills/web-rebuild/scripts/compare_images.py')
compare_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(compare_module)
output = ROOT / 'artifacts/url-inspection'
output.mkdir(parents=True, exist_ok=False)
server = ThreadingHTTPServer(('127.0.0.1', 0), partial(SimpleHTTPRequestHandler, directory=str(ROOT / 'skills/web-rebuild/assets')))
thread = Thread(target=server.serve_forever, daemon=True)
thread.start()
local = f'http://127.0.0.1:{server.server_port}/reference.html'
report = {'purpose': 'URL inspection and comparison controls, not an AI-generated rebuild',
          'os': platform.platform(), 'code_revision': os.getenv('GITHUB_SHA', 'local'), 'captures': []}
def restrict_requests(context, allowed):
    blocked = []

    def handle(route):
        url = route.request.url.split('#', 1)[0]
        if url not in allowed:
            blocked.append(url)
            route.abort()
            return
        # Fetch at most this URL; do not follow redirects before scope checks.
        response = route.fetch(max_redirects=0)
        if 300 <= response.status < 400:
            blocked.append(url + ' [redirect rejected]')
            route.abort()
            return
        route.fulfill(response=response)

    context.route('**/*', handle)
    return blocked


try:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        report['browser'] = browser.version
        sources = [('loopback', local)]
        # External connectivity is tested only on trusted main runs, never on PRs.
        if os.getenv('CHECK_PUBLIC_REFERENCE') == '1':
            sources.append(('public', PUBLIC))
        for label, url in sources:
            for width, height in [(320, 900), (768, 1024), (1440, 1000)]:
                context = browser.new_context(viewport={'width': width, 'height': height}, device_scale_factor=1,
                                              color_scheme='light', reduced_motion='reduce', locale='en-US', timezone_id='UTC', service_workers='block')
                blocked = restrict_requests(context, {url})
                page = context.new_page()
                errors = []
                page.on('pageerror', lambda error: errors.append(str(error)))
                response = page.goto(url, wait_until='load', timeout=45000)
                assert response and response.status == 200, f'Cannot inspect {url}'
                assert page.url == url, f'Unexpected redirect: {page.url}'
                assert page.title().startswith('Fieldnotes Studio'), 'Not the expected reference'
                page.evaluate('document.fonts.ready')
                heading = page.locator('h1')
                assert 'Less noise.' in heading.inner_text(), 'Unexpected source content'
                observed = heading.evaluate('node => { const s = getComputedStyle(node); const r = node.getBoundingClientRect(); return {text:node.innerText,font:s.fontFamily,fontSize:s.fontSize,color:s.color,bounds:{x:r.x,y:r.y,width:r.width,height:r.height}} }')
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
                source = output / f'{label}-{width}-source.png'
                control = output / f'{label}-{width}-control.png'
                page.screenshot(path=str(source), animations='disabled', scale='css')
                page.screenshot(path=str(control), animations='disabled', scale='css')
                assert compare_module.compare(source, control, output / f'{label}-{width}-control')['passed']
                change = page.add_style_tag(content='h1 { color: #0044ff !important; }')
                mutated = output / f'{label}-{width}-mutated.png'
                page.screenshot(path=str(mutated), animations='disabled', scale='css')
                assert not compare_module.compare(source, mutated, output / f'{label}-{width}-mutation')['passed']
                change.evaluate('(node) => node.remove()')
                page.locator('nav a[href="#work"]').click()
                assert page.url == url + '#work'
                summary = page.locator('summary').first
                summary.focus()
                page.keyboard.press('Enter')
                assert page.locator('details').first.evaluate('(node) => node.open')
                assert not errors, errors
                outside = url.rsplit('/', 1)[0] + '/out-of-scope-probe'
                assert page.evaluate('(url) => fetch(url).then(() => false).catch(() => true)', outside)
                assert outside in blocked
                report['captures'].append({'source': label, 'requested_url': url, 'status': response.status,
                    'viewport': {'width': width, 'height': height}, 'dpr': 1, 'locale': 'en-US', 'timezone': 'UTC',
                    'color_scheme': 'light', 'reduced_motion': 'reduce', 'observed_heading': observed,
                    'reference': source.name, 'control': control.name, 'mutated': mutated.name,
                    'same_page_control_passed': True, 'mutation_detected': True,
                    'anchor_navigation': True, 'keyboard_disclosure': True, 'scope_probe_blocked': True, 'blocked_requests': blocked})
                context.close()
        context = browser.new_context(service_workers='block')
        missing_url = local.replace('reference.html', 'missing-reference.html')
        restrict_requests(context, {missing_url})
        page = context.new_page()
        missing = page.goto(missing_url)
        assert missing and missing.status == 404
        report['negative_control'] = {'status': missing.status, 'treated_as_reference': False}
        context.close()
        browser.close()
finally:
    server.shutdown()
    server.server_close()
    thread.join(timeout=5)
    (output / 'report.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(f'URL inspection: {len(report["captures"])} capture cases, difference controls, interactions and 404 check passed.')
