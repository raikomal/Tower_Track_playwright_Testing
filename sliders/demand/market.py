import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://103.204.95.212:8084/")
    page.get_by_role("textbox", name="Username or email").click()
    page.get_by_role("textbox", name="Username or email").fill("user@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("12345")
    page.get_by_role("button", name="LOGIN").click()
    page.locator("div").filter(has_text=re.compile(r"^Market Intelligence$")).first.click()
    page.locator("path:nth-child(4)").first.click()
    page.get_by_role("img", name="USA, z: 5,114. Data Points.").click()
    page.get_by_role("img", name="IRL, z: 538. Data Points.").click()
    page.get_by_role("button", name="Competitor").click()
    page.get_by_role("checkbox", name="ISG").click()
    page.get_by_role("button", name="Search").click()
    page.get_by_role("img", name="IRL, z: 129. Data Points.").click()
    page.get_by_role("img", name="CHN, z: 57. Data Points.").click()
    page.get_by_role("combobox").first.select_option("topic_discovery")
    page.locator(".highcharts-series.highcharts-series-4 > .highcharts-tracker-line").click()
    page.locator(".flex.items-center.ml-auto > .relative > .text-lg").click()
    page.get_by_role("combobox").nth(1).select_option("A34SNO")
    page.locator(".relative.flex > .text-xl").click()
    page.get_by_role("img", name="Tuesday, 31 Mar 2020, 9.8.").click()
    page.get_by_role("img", name="Wednesday, 30 Nov 2022, 13.37").click()
    page.locator(".flex.items-center > button").click()
    page.locator("form").get_by_role("combobox").select_option("health")
    page.get_by_role("img", name="Monday, 30 Nov 2020, 11.54.").click()
    page.get_by_role("img", name="Thursday, 30 Jun 2022, 13.1.").click()
    with page.expect_popup() as page1_info:
        page.locator(".flex.items-center.justify-between > .text-lg").click()
    page1 = page1_info.value
    page1.goto("http://103.204.95.212:8084/market_indicator")
    page1 = page1_info.value
    time.sleep(2)
    chart = page1.locator(".highcharts-container svg")

    chart.hover(position={"x": 350, "y": 220})
    page1.wait_for_timeout(200)

    print(page1.locator(".highcharts-tooltip").inner_text())

    time.sleep(2)
    page1.locator(".highcharts-markers.highcharts-series-0.highcharts-line-series.highcharts-tracker.highcharts-series-hover > .highcharts-halo").click()

    time.sleep(2)
    page1.locator(".highcharts-point.highcharts-internal-node-interactive.highcharts-point-hover").click()
    page1.locator(".highcharts-series.highcharts-series-0.highcharts-line-series.highcharts-series-hover > .highcharts-tracker-line").click()
    page1.get_by_text("Created with Highcharts 11.4.8Growth RateIndexFinanceJan 2018Jan 2019Jan").click()
    page1.locator(".highcharts-markers.highcharts-series-0.highcharts-line-series.highcharts-tracker.highcharts-series-hover > .highcharts-halo").click()
    page1.locator(".highcharts-series.highcharts-series-0.highcharts-line-series.highcharts-series-hover > .highcharts-tracker-line").click()
    page1.locator(".highcharts-series.highcharts-series-0.highcharts-line-series.highcharts-series-hover > .highcharts-tracker-line").click()
    page1.locator(".highcharts-series.highcharts-series-0.highcharts-line-series.highcharts-series-hover > .highcharts-tracker-line").click()
    page1.locator(".highcharts-series.highcharts-series-0.highcharts-line-series.highcharts-series-hover > .highcharts-tracker-line").click()
    page1.locator(".highcharts-series.highcharts-series-0.highcharts-line-series.highcharts-series-hover > .highcharts-tracker-line").click()
    page1.get_by_role("button", name="listIcon").click()
    page1.get_by_role("textbox").first.fill("2016-01-19")
    page1.get_by_role("textbox").nth(1).fill("2026-01-13")
    page1.get_by_role("button", name="Search").click()
    page1.get_by_role("button", name="Next", exact=True).click()
    page1.locator(".highcharts-series.highcharts-series-0.highcharts-line-series.highcharts-series-hover > .highcharts-tracker-line").click()
    page1.locator(".highcharts-series.highcharts-series-0.highcharts-line-series.highcharts-series-hover > .highcharts-tracker-line").click()
    page1.get_by_role("img", name="01-01-2021, 91.268. Internet").click()
    page1.get_by_role("img", name="31-10-2018, 6,067. Asset-").click()
    page1.get_by_role("img", name="30-09-2019, 2,018.987613.").click()
    page.get_by_role("img", name="HomeMenu").click()
    page.locator("div").filter(has_text=re.compile(r"^Demand Intelligence$")).first.click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
