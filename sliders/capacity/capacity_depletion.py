# # import re
# # from playwright.sync_api import Playwright, sync_playwright, expect


# # def run(playwright: Playwright) -> None:
# #     browser = playwright.chromium.launch(headless=False)
# #     context = browser.new_context()
# #     page = context.new_page()
# #     page.goto("http://103.204.95.212:8084/")
# #     page.get_by_role("textbox", name="Username or email").click()
# #     page.get_by_role("textbox", name="Username or email").fill("user@gmail.com")
# #     page.get_by_role("textbox", name="Password").click()
# #     page.get_by_role("textbox", name="Password").fill("12345")
# #     page.get_by_role("checkbox", name="Remember Me").check()
# #     page.get_by_role("button", name="LOGIN").click()
# #     page.get_by_role("button", name="Capacity Insights").click()
# #     page.get_by_role("img", name="Capacity Depletion").click()
# #     page.get_by_text("Created with Highcharts 11.4.8Power Demand (MW)Confidence IntervalActual").click()
# #     page.get_by_role("img", name="Apr-2030, 163,056.7857969699").click()
# #     page.get_by_role("img", name="Nov-2029, 158,750.20005001032").click()
# #     # page.get_by_role("button", name="Shows the probability of").click()
# #     page.get_by_role("button").first.click()
# #     page.get_by_role("textbox").first.fill("2019-01-02")
# #     page.get_by_role("textbox").nth(1).fill("2030-12-30")
# #     page.get_by_role("combobox").first.select_option("2")
# #     page.get_by_role("combobox").nth(1).select_option("2")
# #     page.get_by_role("button", name="Search").click()
# #     # page.get_by_role("img", name="Aug-2030, 164,167.50595020907").click()
# #     # page.get_by_role("img", name="Apr-2030, 164,240.79676899564").click()
# #     # page.get_by_role("img", name="Dec-2029, 143,920.53185384264").click()
# #     page.locator("div:nth-child(3) > .relative > .text-white.text-2xl").first.click()
# #     page.locator(".highcharts-markers.highcharts-series-0.highcharts-line-series.highcharts-tracker.highcharts-series-hover > .highcharts-point").click()
# #     page.locator(".highcharts-markers.highcharts-series-0.highcharts-line-series.highcharts-tracker.highcharts-series-hover > .highcharts-point").click()
# #     page.locator(".flex.items-center.justify-center.gap-3 > button").click()
# #     page.get_by_role("paragraph").filter(has_text="Start Date -").get_by_role("textbox").fill("2023-01-03")
# #     page.get_by_role("paragraph").filter(has_text="End Date -").get_by_role("textbox").fill("2025-02-27")
# #     page.get_by_role("combobox").first.select_option("Facility2")
# #     page.get_by_role("button", name="Search").click()
# #     page.locator(".highcharts-markers.highcharts-series-0.highcharts-line-series.highcharts-tracker.highcharts-series-hover > .highcharts-point").click()
# #     page.locator(".highcharts-halo").click()
# #     page.locator("div:nth-child(2) > .relative > .text-white.text-2xl").click()
# #     page.locator("div:nth-child(2) > .relative > .text-white.text-2xl").click()
# #     page.get_by_role("img", name="-07, 50.67. Growth Rate.").click()
# #     page.get_by_role("img", name="-04, 49.95. Growth Rate.").click()
# #     page.get_by_role("img", name="-10, 48.54. Growth Rate.").click()
# #     page.locator(".w-full.flex.flex-wrap > .flex-1 > .relative.text-\\[\\#182533\\] > .flex > button").click()
# #     page.get_by_role("paragraph").filter(has_text="Start Date -").get_by_role("textbox").fill("2018-02-01")
# #     page.get_by_role("paragraph").filter(has_text="End Date -").get_by_role("textbox").fill("2025-02-27")
# #     page.get_by_role("combobox").first.select_option("yearly")
# #     page.get_by_role("combobox").nth(1).select_option("Customer4")
# #     page.locator(".flex > .flex.justify-center > button").click()
# #     page.get_by_role("textbox").first.fill("2023-01-04")
# #     page.get_by_role("textbox").nth(1).fill("2025-02-26")
# #     page.get_by_role("combobox").first.select_option("FEDFUNDS")
# #     page.get_by_role("combobox").nth(1).select_option("C2")
# #     page.get_by_role("combobox").nth(2).select_option("F2")
# #     page.get_by_role("button", name="Search").click()
# #     page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.000").click()
# #     page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.003").click()
# #     page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.004").click()

# #     # ---------------------
# #     context.close()
# #     browser.close()


# # with sync_playwright() as playwright:
# #     run(playwright)
# # from core.navigation import open_capacity_depletion, go_back
# from core.actions import step_click, step_fill, step_select, logger


# def run(page):
#     """
#     Capacity Depletion – Capacity Insights
#     Minimal-change refactor
#     """

#     logger.info("📉 Capacity Depletion started")

#     # ---------------- OPEN TILE ----------------
#     open_capacity_depletion(page)

#     # ---------------- CHART INTERACTIONS ----------------
#     step_click(
#         page.get_by_text(
#             "Created with Highcharts 11.4.8Power Demand (MW)Confidence IntervalActual"
#         ),
#         "Capacity depletion chart"
#     )

#     step_click(
#         page.get_by_role("img", name="Apr-2030, 163,056.7857969699"),
#         "Apr 2030 data point"
#     )

#     step_click(
#         page.get_by_role("img", name="Nov-2029, 158,750.20005001032"),
#         "Nov 2029 data point"
#     )

#     # ---------------- DATE FILTER ----------------
#     step_click(
#         page.get_by_role("button").first,
#         "Open date filter"
#     )

#     step_fill(
#         page.get_by_role("textbox").first,
#         "2019-01-02",
#         "Start date"
#     )

#     step_fill(
#         page.get_by_role("textbox").nth(1),
#         "2030-12-30",
#         "End date"
#     )

#     step_select(
#         page.get_by_role("combobox").first,
#         "2",
#         "Granularity dropdown"
#     )

#     step_select(
#         page.get_by_role("combobox").nth(1),
#         "2",
#         "Metric dropdown"
#     )

#     step_click(
#         page.get_by_role("button", name="Search"),
#         "Search capacity data"
#     )

#     # ---------------- DETAIL VIEW ----------------
#     step_click(
#         page.locator("div:nth-child(3) > .relative > .text-white.text-2xl").first,
#         "Expand capacity details"
#     )

#     step_click(
#         page.locator(
#             ".highcharts-markers.highcharts-series-0.highcharts-line-series."
#             "highcharts-tracker.highcharts-series-hover > .highcharts-point"
#         ),
#         "Capacity chart point"
#     )

#     step_click(
#         page.locator(".flex.items-center.justify-center.gap-3 > button"),
#         "Open facility filter"
#     )

#     step_fill(
#         page.get_by_role("paragraph")
#         .filter(has_text="Start Date -")
#         .get_by_role("textbox"),
#         "2023-01-03",
#         "Facility start date"
#     )

#     step_fill(
#         page.get_by_role("paragraph")
#         .filter(has_text="End Date -")
#         .get_by_role("textbox"),
#         "2025-02-27",
#         "Facility end date"
#     )

#     step_select(
#         page.get_by_role("combobox").first,
#         "Facility2",
#         "Facility dropdown"
#     )

#     step_click(
#         page.get_by_role("button", name="Search"),
#         "Search facility data"
#     )

#     # ---------------- GROWTH RATE ----------------
#     step_click(
#         page.locator("div:nth-child(2) > .relative > .text-white.text-2xl"),
#         "Open growth rate view"
#     )

#     step_click(
#         page.get_by_role("img", name="-07, 50.67. Growth Rate."),
#         "Growth rate point 1"
#     )

#     step_click(
#         page.get_by_role("img", name="-04, 49.95. Growth Rate."),
#         "Growth rate point 2"
#     )

#     step_click(
#         page.get_by_role("img", name="-10, 48.54. Growth Rate."),
#         "Growth rate point 3"
#     )

#     # ---------------- ECONOMIC FACTORS ----------------
#     step_click(
#         page.locator(
#             ".w-full.flex.flex-wrap > .flex-1 > "
#             ".relative.text-\\[\\#182533\\] > .flex > button"
#         ),
#         "Open economic factors"
#     )

#     step_fill(
#         page.get_by_role("paragraph")
#         .filter(has_text="Start Date -")
#         .get_by_role("textbox"),
#         "2018-02-01",
#         "Economic start date"
#     )

#     step_fill(
#         page.get_by_role("paragraph")
#         .filter(has_text="End Date -")
#         .get_by_role("textbox"),
#         "2025-02-27",
#         "Economic end date"
#     )

#     step_select(
#         page.get_by_role("combobox").first,
#         "yearly",
#         "Frequency dropdown"
#     )

#     step_select(
#         page.get_by_role("combobox").nth(1),
#         "Customer4",
#         "Customer dropdown"
#     )

#     step_click(
#         page.locator(".flex > .flex.justify-center > button"),
#         "Apply economic filters"
#     )

#     # ---------------- RATE ANALYSIS ----------------
#     step_fill(
#         page.get_by_role("textbox").first,
#         "2023-01-04",
#         "Rate start date"
#     )

#     step_fill(
#         page.get_by_role("textbox").nth(1),
#         "2025-02-26",
#         "Rate end date"
#     )

#     step_select(
#         page.get_by_role("combobox").first,
#         "FEDFUNDS",
#         "Indicator dropdown"
#     )

#     step_select(
#         page.get_by_role("combobox").nth(1),
#         "C2",
#         "Category dropdown"
#     )

#     step_select(
#         page.get_by_role("combobox").nth(2),
#         "F2",
#         "Frequency dropdown"
#     )

#     step_click(
#         page.get_by_role("button", name="Search"),
#         "Search rate data"
#     )

#     step_click(
#         page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.000"),
#         "Rate point 1"
#     )

#     step_click(
#         page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.003"),
#         "Rate point 2"
#     )

#     step_click(
#         page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.004"),
#         "Rate point 3"
#     )

#     # ---------------- BACK ----------------
#     go_back(page)

#     logger.info("✅ Capacity Depletion completed")
