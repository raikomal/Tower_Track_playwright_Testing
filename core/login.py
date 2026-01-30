from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from core.actions import step_fill, step_click, logger
from core.actions import step_fill, step_click, logger, set_context

USERNAME = "user@gmail.com"
PASSWORD = "12345"


def login(page):
    """
    Performs login only if user is not already logged in.
    Uses step-based logging + CSV recording.
    """

    # 🔹 Set LOGIN context
    set_context(
        application="Authentication",
        micro_application="Login",
        title="Login Validation"
    )

    try:
        # If dashboard already visible, skip login
        page.wait_for_selector("text=Demand Insights", timeout=5000)
        logger.info("✅ Already logged in, skipping login")
        return
    except PlaywrightTimeoutError:
        pass

    logger.info("Performing login")

    # Username
    step_fill(
        page.get_by_role("textbox", name="Username or email"),
        USERNAME,
        "Username textbox"
    )

    # Password
    step_fill(
        page.get_by_role("textbox", name="Password"),
        PASSWORD,
        "Password textbox"
    )

    # Remember Me
    remember_me = page.get_by_role("checkbox", name="Remember Me")
    if remember_me.is_visible() and not remember_me.is_checked():
        step_click(remember_me, "Remember Me checkbox")

    # Login
    step_click(
        page.get_by_role("button", name="LOGIN"),
        "LOGIN button"
    )

    # Wait for dashboard
    page.wait_for_load_state("networkidle")
    page.wait_for_selector("text=Demand Insights", timeout=15000)

    logger.info(" Dashboard loaded — starting Demand Insights flow")
