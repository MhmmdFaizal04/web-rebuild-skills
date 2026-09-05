"""Exercise the static showcase separately from the practice reference."""
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
with sync_playwright() as p:
    browser = p.chromium.launch()
    for width, height in [(320,900),(768,1024),(1440,1000)]:
        context = browser.new_context(viewport={'width':width,'height':height}, reduced_motion='reduce')
        page = context.new_page()
        errors = []
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.goto((ROOT / '_site/index.html').as_uri())
        page.evaluate('document.fonts.ready')
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), f'Overflow {width}'
        assert page.locator('img').evaluate_all('(images) => images.every(i => i.complete && i.naturalWidth > 0)')
        assert page.locator('#copy').is_visible()
        page.evaluate("Object.defineProperty(navigator, 'clipboard', {configurable:true,value:{writeText:async (text)=>{window.copiedCommand=text}}})")
        page.locator('#copy').click()
        page.wait_for_function("window.copiedCommand === document.getElementById('command').textContent")
        assert page.locator('#copy-status').inner_text() == 'Installation command copied.'
        page.evaluate("Object.defineProperty(navigator, 'clipboard', {configurable:true,value:{writeText:async()=>{throw new Error('denied')}}})")
        page.locator('#copy').click()
        page.wait_for_function("document.getElementById('copy-status').textContent.includes('Clipboard unavailable')")
        assert page.evaluate('getSelection().toString() === document.getElementById("command").textContent')
        assert 'sr-only' not in page.locator('#copy-status').get_attribute('class')
        assert page.locator('#copy').inner_text() == 'Retry copy'
        page.reload()
        page.evaluate('document.fonts.ready')
        page.locator('summary').first.focus()
        page.keyboard.press('Enter')
        assert page.locator('details').first.evaluate('(node)=>node.open')
        page.keyboard.press('Enter')
        page.locator('summary').first.evaluate('(node) => node.blur()')
        page.evaluate('scrollTo(0,0)')
        page.screenshot(path=str(ROOT / f'artifacts/showcase-{width}.png'), full_page=True, animations='disabled')
        assert not errors, errors
        context.close()
    context = browser.new_context(java_script_enabled=False, viewport={'width':320,'height':900})
    page = context.new_page()
    page.goto((ROOT / '_site/index.html').as_uri())
    assert page.locator('#command').is_visible()
    assert not page.locator('#copy').is_visible()
    assert page.locator('nav a').count() == 3
    context.close()
    browser.close()
print('Showcase: 3 viewport checks, loaded preview, clipboard success/failure, disclosure, and no-JS fallback passed.')
