# import re
# import time
# from playwright.sync_api import Playwright, sync_playwright, expect


# # def run(playwright: Playwright) -> None:
# #     browser = playwright.chromium.launch(headless=False)
# #     context = browser.new_context()
# #     page = context.new_page()
# #     page.goto("http://103.204.95.212:8084/")
# #     page.get_by_role("textbox", name="Username or email").click()
# #     page.get_by_role("textbox", name="Username or email").fill("user@gmail.com")
# #     page.get_by_role("textbox", name="Username or email").press("Tab")
# #     page.get_by_role("textbox", name="Password").fill("12345")
# #     page.get_by_role("button", name="LOGIN").click()
# #     page.locator("div").filter(has_text=re.compile(r"^Demand Intelligence$")).first.click()
# #     page.get_by_role("region", name="Predicted Power Usage, series").get_by_label("Dec-2023, 82,867.83890246053").click()
# #     page.get_by_role("region", name="Predicted Power Usage, series").get_by_label("Apr-2026, 116,976.5027856621").click()
# #     page.get_by_text("Created with Highcharts 11.4.8Power Demand(MW)Confidence IntervalActual Power").click()
# #     page.get_by_text("Created with Highcharts 11.4.8Mean Factor ImpactAnnotation").click()
# #     page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.003, -0.26. ECOMPCTSA.").click()
# #     page.get_by_text("Created with Highcharts 11.4.8Mean Factor ImpactAnnotation").click()
# #     page.get_by_role("region", name="Actual Power Usage, bar").get_by_label("Nov-2024, 93,269.06937795535").click()
# #     page.get_by_text("Created with Highcharts 11.4.8PowerDemand (MW)Actual Power UsagePredicted Power").click()
# #     page.locator(".highcharts-series.highcharts-series-5 > .highcharts-tracker-line").click()

# #     # -------------
# #     context.close()
# #     browser.close()


# # with sync_playwright() as playwright:
# #     run(playwright)
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
#     page.get_by_role("img", name="Demand Intelligence").click()
#     page.get_by_role("img").nth(5).click()
#     page.get_by_role("region", name="Predicted Power Usage, series").get_by_label("Nov-2027, 147,313.5204880285").click()
#     page.get_by_role("region", name="Predicted Power Usage, series").get_by_label("Oct-2027, 145,889.63391808706").click()
#     page.get_by_role("region", name="Predicted Power Usage, series").get_by_label("Jul-2027, 140,988.66762298543").click()
#     page.get_by_role("region", name="Predicted Power Usage, series").get_by_label("Mar-2027, 136,025.39868156388").click()
#     page.get_by_role("button").first.click()
#     page.get_by_role("textbox").first.fill("2023-01-02")
#     page.get_by_role("textbox").nth(1).fill("2027-12-30")
#     page.get_by_role("combobox").first.select_option("2")
#     page.get_by_role("combobox").nth(1).select_option("2")
#     page.get_by_role("button", name="Search").click()
#     page.get_by_role("img", name="Aug-2027, 117,044.2335791888").click()
#     page.get_by_role("img", name="Jun-2027, 117,155.903932565.").click()
#     page.get_by_text("Created with Highcharts 11.4.8Power Demand(MW)Confidence IntervalActual Power").click()
#     page.locator(".flex.items-center.justify-center > .relative > .text-white.text-2xl").first.click()
#     page.get_by_role("img", name="Dec-2027, 149,249.98135933795").click()
#     page.get_by_text("Created with Highcharts 11.4.8Power Demand(MW)Actual Power UsagePredicted Power").click()
#     page.locator(".flex.items-center.justify-center.gap-3 > button").click()
#     page.get_by_role("combobox").select_option("2")
#     page.get_by_role("paragraph").filter(has_text="Start Date -").get_by_role("textbox").fill("2023-01-03")
#     page.get_by_role("paragraph").filter(has_text="End Date -").get_by_role("textbox").fill("2027-12-31")
#     page.get_by_role("button", name="Search").click()
#     page.get_by_role("region", name="Predicted Power Usage, bar").get_by_label("Jan-2023, 71,801.08376355526").click()
#     page.get_by_text("Created with Highcharts 11.4.8PowerDemand (MW)Actual Power UsagePredicted Power").click()
#     page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.000, -1.72. GDP.").click()
#     page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.001, 1.19. GDP.").click()
#     page.get_by_text("Created with Highcharts 11.4.8Mean FactorImpactAnnotation").click()
#     page.locator(".text-white.text-4xl").click()
#     page.locator(".flex.items-center.justify-end > button").click()
    
#     page.locator(".flex.items-center.justify-center.gap-3 > button").click()
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
#     page.locator(".text-xl.mx-2.flex.items-center.justify-center > .relative > .text-white.text-2xl").click()
#     # time.sleep(1)
#     page.get_by_role("img", name="July 2019, 22.22. Retail.").nth(2).click()
#     page.locator(".flex-1 > button").click()
#     page.get_by_role("combobox").first.select_option("Retail")
#     # time.sleep(1)
#     page.get_by_role("combobox").nth(1).select_option("monthly")
#     # time.sleep(1)
#     page.get_by_text("Created with Highcharts 11.4.8Growth RateRetailJan 2018Jan 2019Jan 2020Jan").click()
#     time.sleep(2)
#     page.get_by_role("img", name="Wednesday, 31 Jan 2018, 0.").click()
#     time.sleep(2)

#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
import time
from core.navigation import open_demand_intelligence, go_back
from core.actions import step_click, step_fill, step_select, logger


def run(page):
    """
    Demand Intelligence – Demand Insights
    Minimal-change refactor (WORKING)
    """

    logger.info("📈 Demand Intelligence started")


    # ✅ wait for charts to render
    page.wait_for_selector(".highcharts-series", timeout=15000)

    # ---------------- CHART INTERACTIONS ----------------
    step_click(
        page.get_by_role("img").nth(5),
        "Demand Intelligence expand icon"
    )

    page.wait_for_selector("text=Predicted Power", timeout=15000)

    step_click(
        page.get_by_role("region", name="Predicted Power Usage, series")
        .get_by_label("Nov-2027, 147,313.5204880285"),
        "Predicted Power Nov 2027"
    )

    step_click(
        page.get_by_role("region", name="Predicted Power Usage, series")
        .get_by_label("Oct-2027, 145,889.63391808706"),
        "Predicted Power Oct 2027"
    )

    step_click(
        page.get_by_role("region", name="Predicted Power Usage, series")
        .get_by_label("Jul-2027, 140,988.66762298543"),
        "Predicted Power Jul 2027"
    )

    step_click(
        page.get_by_role("region", name="Predicted Power Usage, series")
        .get_by_label("Mar-2027, 136,025.39868156388"),
        "Predicted Power Mar 2027"
    )

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
        "2027-12-30",
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
        "Search demand data"
    )

    page.wait_for_selector(".highcharts-series", timeout=15000)

    # ---------------- DATA POINTS ----------------
    step_click(
        page.get_by_role("img", name="Aug-2027, 117,044.2335791888"),
        "Aug 2027 data point"
    )

    step_click(
        page.get_by_role("img", name="Jun-2027, 117,155.903932565."),
        "Jun 2027 data point"
    )

    step_click(
        page.locator(
            ".flex.items-center.justify-center > .relative > .text-white.text-2xl"
        ).first,
        "Expand actual vs predicted chart"
    )

    step_click(
        page.get_by_role("img", name="Dec-2027, 149,249.98135933795"),
        "Dec 2027 data point"
    )

    # ---------------- FACTOR ANALYSIS ----------------
    step_click(
        page.locator(".flex.items-center.justify-center.gap-3 > button"),
        "Open factor analysis"
    )

    page.wait_for_selector(".highcharts-series", timeout=15000)

    step_select(
        page.get_by_role("combobox"),
        "2",
        "Factor dropdown"
    )

    step_fill(
        page.get_by_role("paragraph")
        .filter(has_text="Start Date -")
        .get_by_role("textbox"),
        "2023-01-03",
        "Factor start date"
    )

    step_fill(
        page.get_by_role("paragraph")
        .filter(has_text="End Date -")
        .get_by_role("textbox"),
        "2027-12-31",
        "Factor end date"
    )

    step_click(
        page.get_by_role("button", name="Search"),
        "Search factor data"
    )

    step_click(
        page.get_by_role("img", name="Jan-2023, 71,801.08376355526"),
        "Jan 2023 bar"
    )

    # ---------------- ECONOMIC FACTORS ----------------
    step_click(
        page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.000, -1.72. GDP."),
        "GDP negative impact"
    )

    step_click(
        page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.001, 1.19. GDP."),
        "GDP positive impact"
    )

    step_click(
        page.locator(".text-white.text-4xl"),
        "Close factor popup"
    )

    # ---------------- RETAIL ANALYSIS ----------------
    step_click(
        page.locator(".flex.items-center.justify-end > button"),
        "Open retail analysis"
    )

    step_fill(
        page.get_by_role("textbox").first,
        "2023-01-02",
        "Retail start date"
    )

    step_fill(
        page.get_by_role("textbox").nth(1),
        "2025-02-27",
        "Retail end date"
    )

    step_select(
        page.get_by_role("combobox").first,
        "FEDFUNDS",
        "Retail indicator"
    )

    step_select(
        page.get_by_role("combobox").nth(1),
        "C2",
        "Retail category"
    )

    step_select(
        page.get_by_role("combobox").nth(2),
        "F2",
        "Retail frequency"
    )

    step_click(
        page.get_by_role("button", name="Search"),
        "Search retail data"
    )

    step_click(
        page.get_by_role("img", name="July 2019, 22.22. Retail.").nth(2),
        "Retail July 2019"
    )

    # ---------------- EXIT ----------------
    step_click(
        page.get_by_role("img", name="HomeMenu"),
        "Home menu (exit Demand Intelligence)"
    )

    page.wait_for_selector("text=Demand Intelligence", timeout=15000)

    logger.info("✅ Demand Intelligence completed")
