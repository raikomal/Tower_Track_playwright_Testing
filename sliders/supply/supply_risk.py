# import re
# from playwright.sync_api import Playwright, sync_playwright, expect


# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("http://103.204.95.212:8084/")
#     page.get_by_role("textbox", name="Username or email").click()
#     page.get_by_role("textbox", name="Username or email").fill("user@gmail.com")
#     page.get_by_role("textbox", name="Password").click()
#     page.get_by_role("textbox", name="Password").fill("12345")
#     page.get_by_role("checkbox", name="Remember Me").check()
#     page.get_by_role("button", name="LOGIN").click()
#     page.get_by_role("button", name="Supply Insights").click()
#     page.get_by_role("img", name="Supply Risk Assessment").click()
#     page.get_by_role("button").nth(4).click()
#     page.locator("div:nth-child(7)").first.click()
#     page.locator("div:nth-child(18)").click()
#     page.get_by_role("combobox").select_option("transformer")
#     page.get_by_role("combobox").select_option("generator")
#     page.locator(".text-white.text-2xl").first.click()
#     page.get_by_role("img", name="x, 5, 0.57. Probability").click()
#     page.get_by_role("img", name="x, 1, 0.83. Probability").click()
#     page.locator("button").first.click()
#     page.locator("span").filter(has_text="Estimated Delivery").get_by_role("combobox").select_option("ordersize")
#     page.locator(".highcharts-series.highcharts-series-2 > .highcharts-tracker-line").click()
#     page.locator("button").first.click()
#     page.locator("span").filter(has_text="Estimated Delivery").get_by_role("combobox").select_option("scgeorisk")
#     page.get_by_role("img", name="x, 5, 0.57. Probability").click()
#     page.locator(".flex > .flex.justify-between > .flex.font-bold > .relative > .text-white.text-2xl").first.click()
#     # page.locator("#id-514 circle").click()
#     # page.locator("#id-526 circle").click()

#     # page.locator("#id-538 > circle").click()
#     # page.locator("#id-510 circle").click()
#     page.locator(".flex.border.border-\\[\\#545454\\].border-opacity-75.bg-gradient-to-b > .flex.justify-between > .flex.font-bold > .relative > .text-white.text-2xl").click()
#     page.get_by_role("img", name="Material SC Risk, 0.5.").click()
#     page.get_by_role("img", name="Order Size, 0.1. Negative").click()
#     page.get_by_role("img", name="SC Geo Risk, 0.4. Negative").click()

#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
from core.navigation import open_supply_risk, go_back
from core.actions import step_click, step_select, logger


def run(page):
    """
    Supply Risk Assessment – Supply Insights
    Minimal-change refactor
    """

    logger.info("⚠️ Supply Risk Assessment started")

    # ---------------- OPEN TILE ----------------
    open_supply_risk(page)

    # ---------------- FILTER & VIEW ----------------
    step_click(
        page.get_by_role("button").nth(4),
        "Open supply risk controls"
    )

    step_click(
        page.locator("div:nth-child(7)").first,
        "Risk category selection 1"
    )

    step_click(
        page.locator("div:nth-child(18)"),
        "Risk category selection 2"
    )

    step_select(
        page.get_by_role("combobox"),
        "transformer",
        "Component dropdown"
    )

    step_select(
        page.get_by_role("combobox"),
        "generator",
        "Component dropdown"
    )

    # ---------------- PROBABILITY VIEW ----------------
    step_click(
        page.locator(".text-white.text-2xl").first,
        "Open probability view"
    )

    step_click(
        page.get_by_role("img", name="x, 5, 0.57. Probability"),
        "Probability point 0.57"
    )

    step_click(
        page.get_by_role("img", name="x, 1, 0.83. Probability"),
        "Probability point 0.83"
    )

    # ---------------- DELIVERY RISK ----------------
    step_click(
        page.locator("button").first,
        "Open delivery risk"
    )

    step_select(
        page.locator("span")
        .filter(has_text="Estimated Delivery")
        .get_by_role("combobox"),
        "ordersize",
        "Estimated delivery – Order size"
    )

    step_click(
        page.locator(
            ".highcharts-series.highcharts-series-2 > .highcharts-tracker-line"
        ),
        "Order size risk curve"
    )

    step_click(
        page.locator("button").first,
        "Open delivery risk again"
    )

    step_select(
        page.locator("span")
        .filter(has_text="Estimated Delivery")
        .get_by_role("combobox"),
        "scgeorisk",
        "Estimated delivery – SC Geo Risk"
    )

    step_click(
        page.get_by_role("img", name="x, 5, 0.57. Probability"),
        "SC Geo Risk probability"
    )

    # ---------------- RISK BREAKDOWN ----------------
    step_click(
        page.locator(
            ".flex > .flex.justify-between > .flex.font-bold > "
            ".relative > .text-white.text-2xl"
        ).first,
        "Open risk breakdown"
    )

    step_click(
        page.locator(
            ".flex.border.border-\\[\\#545454\\].border-opacity-75.bg-gradient-to-b "
            "> .flex.justify-between > .flex.font-bold > .relative > .text-white.text-2xl"
        ),
        "Open detailed risk breakdown"
    )

    step_click(
        page.get_by_role("img", name="Material SC Risk, 0.5."),
        "Material SC Risk"
    )

    step_click(
        page.get_by_role("img", name="Order Size, 0.1. Negative"),
        "Order Size Risk"
    )

    step_click(
        page.get_by_role("img", name="SC Geo Risk, 0.4. Negative"),
        "SC Geo Risk"
    )

    # ---------------- BACK ----------------
    go_back(page)

    logger.info("✅ Supply Risk Assessment completed")
