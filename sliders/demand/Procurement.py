import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://103.204.95.212:8084/")
    page.get_by_role("textbox", name="Username or email").click()
    page.get_by_role("textbox", name="Username or email").fill("user@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("12345")
    page.get_by_role("checkbox", name="Remember Me").check()
    page.get_by_role("button", name="LOGIN").click()
    page.get_by_role("img", name="Procurement Demand Prediction").click()
    # page.get_by_role("button", name="Shows the trend for long-term").click()
    page.get_by_role("img", name="Jan-2030, 158,775.902423034.").click()
    page.get_by_role("img", name="Nov-2029, 158,750.20005001032").click()
    page.get_by_text("Created with Highcharts 11.4.8Capacity Amount(MW)Confidence IntervalActual").click()
    page.get_by_text("Created with Highcharts 11.4.8Capacity Amount(MW)Confidence IntervalActual").click()
    page.get_by_role("button").first.click()
    page.get_by_role("textbox").first.fill("2023-01-02")
    page.get_by_role("textbox").nth(1).fill("2030-12-30")
    page.get_by_role("combobox").first.select_option("2")
    page.get_by_role("combobox").nth(1).select_option("2")
    page.get_by_role("button", name="Search").click()
    page.get_by_text("Created with Highcharts 11.4.8Capacity Amount(MW)Confidence IntervalActual").click()
    page.get_by_text("Created with Highcharts 11.4.8Capacity Amount(MW)Confidence IntervalActual").click()
    page.get_by_role("img", name="Jun-2028, 130,145.57276468628").click()
    page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.005, -1.12. DCOILWTICO.").click()
    page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.004, 0.31. DCOILWTICO.").click()
    page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.003, 0.32. GDP.").click()
    page.locator(".text-white.text-2xl.max-2xl\\:text-lg").first.click()
    page.locator(".flex.items-center.justify-end > button").click()
    page.get_by_role("textbox").first.fill("2023-01-02")
    page.get_by_role("textbox").nth(1).fill("2025-02-27")
    page.get_by_role("combobox").first.select_option("FEDFUNDS")
    page.get_by_role("combobox").nth(1).select_option("C2")
    page.get_by_role("combobox").nth(2).select_option("F2")
    page.get_by_role("button", name="Search").click()
    page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.005").click()
    page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.004").click()
    page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.003").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
