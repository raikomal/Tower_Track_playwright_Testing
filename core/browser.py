from playwright.sync_api import sync_playwright

_playwright = None
_browser = None
_context = None
_page = None


def get_page():
    global _playwright, _browser, _context, _page

    if _page is None:
        _playwright = sync_playwright().start()

        _browser = _playwright.chromium.launch(
            headless=False,
            args=["--start-maximized"]
        )

        _context = _browser.new_context(no_viewport=True)
        _page = _context.new_page()

    return _page


def close_browser():
    global _playwright, _browser, _context, _page

    if _context:
        _context.close()
    if _browser:
        _browser.close()
    if _playwright:
        _playwright.stop()

    _playwright = _browser = _context = _page = None
