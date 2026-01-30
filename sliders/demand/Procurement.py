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
#     page.get_by_role("img", name="Procurement Demand Prediction").click()
#     # page.get_by_role("button", name="Shows the trend for long-term").click()
#     page.get_by_role("img", name="Jan-2030, 158,775.902423034.").click()
#     page.get_by_role("img", name="Nov-2029, 158,750.20005001032").click()
#     page.get_by_text("Created with Highcharts 11.4.8Capacity Amount(MW)Confidence IntervalActual").click()
#     page.get_by_text("Created with Highcharts 11.4.8Capacity Amount(MW)Confidence IntervalActual").click()
#     page.get_by_role("button").first.click()
#     page.get_by_role("textbox").first.fill("2023-01-02")
#     page.get_by_role("textbox").nth(1).fill("2030-12-30")
#     page.get_by_role("combobox").first.select_option("2")
#     page.get_by_role("combobox").nth(1).select_option("2")
#     page.get_by_role("button", name="Search").click()
#     page.get_by_text("Created with Highcharts 11.4.8Capacity Amount(MW)Confidence IntervalActual").click()
#     page.get_by_text("Created with Highcharts 11.4.8Capacity Amount(MW)Confidence IntervalActual").click()
#     page.get_by_role("img", name="Jun-2028, 130,145.57276468628").click()
#     page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.005, -1.12. DCOILWTICO.").click()
#     page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.004, 0.31. DCOILWTICO.").click()
#     page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.003, 0.32. GDP.").click()
#     page.locator(".text-white.text-2xl.max-2xl\\:text-lg").first.click()
#     page.locator(".flex.items-center.justify-end > button").click()
#     page.get_by_role("textbox").first.fill("2023-01-02")
#     page.get_by_role("textbox").nth(1).fill("2025-02-27")
#     page.get_by_role("combobox").first.select_option("FEDFUNDS")
#     page.get_by_role("combobox").nth(1).select_option("C2")
#     page.get_by_role("combobox").nth(2).select_option("F2")
#     page.get_by_role("button", name="Search").click()
#     page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.005").click()
#     page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.004").click()
#     page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.003").click()

#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
from core.navigation import open_procurement
from core.actions import step_click, step_fill, step_select, logger


def run(page):
    """
    Procurement – Demand Insights
    Minimal-change refactor
    """

    logger.info("🧾 Procurement started")

    # ---------------- OPEN TILE ----------------
    open_procurement(page)
    page.wait_for_selector(".highcharts-series", timeout=20000)


    # ---------------- CHART INTERACTIONS ----------------
    step_click(
        page.get_by_role("img", name="Jan-2030, 158,775.902423034."),
        "Jan 2030 data point"
    )

    step_click(
        page.get_by_role("img", name="Nov-2029, 158,750.20005001032"),
        "Nov 2029 data point"
    )

    # step_click(
    #     page.get_by_text(
    #         "Created with Highcharts 11.4.8Capacity Amount(MW)Confidence IntervalActual"
    #     ),
    #     "Capacity chart"
    # )

    # ---------------- DATE FILTER ----------------
    step_click(
        page.get_by_role("button").first,
        "Open date filter"
    )

    step_fill(
        page.get_by_role("textbox").first,
        "2023-01-02",
        "Start date"
    )

    step_fill(
        page.get_by_role("textbox").nth(1),
        "2030-12-30",
        "End date"
    )

    step_select(
        page.get_by_role("combobox").first,
        "2",
        "Granularity dropdown"
    )

    step_select(
        page.get_by_role("combobox").nth(1),
        "2",
        "Metric dropdown"
    )

    step_click(
        page.get_by_role("button", name="Search"),
        "Search procurement data"
    )

    # ---------------- DATA POINTS ----------------
    step_click(
        page.get_by_role("img", name="Jun-2028, 130,145.57276468628"),
        "Jun 2028 data point"
    )

    # step_click(
    #     page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.005, -1.12. DCOILWTICO."),
    #     "Oil price negative impact"
    # )

    # step_click(
    #     page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.004, 0.31. DCOILWTICO."),
    #     "Oil price positive impact"
    # )

    # step_click(
    #     page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.003, 0.32. GDP."),
    #     "GDP impact"
    # )

    step_click(
        page.locator(".text-white.text-2xl.max-2xl\\:text-lg").first,
        "Close impact popup"
    )

    # ---------------- RETAIL / RATE ANALYSIS ----------------
    step_click(
        page.locator(".flex.items-center.justify-end > button"),
        "Open rate analysis"
    )

    step_fill(
        page.get_by_role("textbox").first,
        "2023-01-02",
        "Rate start date"
    )

    step_fill(
        page.get_by_role("textbox").nth(1),
        "2025-02-27",
        "Rate end date"
    )

    step_select(
        page.get_by_role("combobox").first,
        "FEDFUNDS",
        "Indicator dropdown"
    )

    step_select(
        page.get_by_role("combobox").nth(1),
        "C2",
        "Category dropdown"
    )

    step_select(
        page.get_by_role("combobox").nth(2),
        "F2",
        "Frequency dropdown"
    )

    step_click(
        page.get_by_role("button", name="Search"),
        "Search rate data"
    )

    step_click(
        page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.005"),
        "Rate data point 1"
    )

    step_click(
        page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.004"),
        "Rate data point 2"
    )

    step_click(
        page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.003"),
        "Rate data point 3"
    )

    # ---------------- BACK ----------------
   

    logger.info("✅ Procurement completed")
    step_click(
    page.locator("//img[@alt='HomeMenu']"),
    "Home menu (exit Procurement)"
)

    # wait until Demand tiles are visible
    page.wait_for_selector("text=Demand Intelligence", timeout=15000)


