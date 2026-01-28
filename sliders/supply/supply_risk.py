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
    page.get_by_role("button", name="Supply Insights").click()
    page.get_by_role("img", name="Supply Risk Assessment").click()
    page.get_by_role("button").nth(4).click()
    page.locator("div:nth-child(7)").first.click()
    page.locator("div:nth-child(18)").click()
    page.get_by_role("combobox").select_option("transformer")
    page.get_by_role("combobox").select_option("generator")
    page.locator(".text-white.text-2xl").first.click()
    page.get_by_role("img", name="x, 5, 0.57. Probability").click()
    page.get_by_role("img", name="x, 1, 0.83. Probability").click()
    page.locator("button").first.click()
    page.locator("span").filter(has_text="Estimated Delivery").get_by_role("combobox").select_option("ordersize")
    page.locator(".highcharts-series.highcharts-series-2 > .highcharts-tracker-line").click()
    page.locator("button").first.click()
    page.locator("span").filter(has_text="Estimated Delivery").get_by_role("combobox").select_option("scgeorisk")
    page.get_by_role("img", name="x, 5, 0.57. Probability").click()
    page.locator(".flex > .flex.justify-between > .flex.font-bold > .relative > .text-white.text-2xl").first.click()
    # page.locator("#id-514 circle").click()
    # page.locator("#id-526 circle").click()

    # page.locator("#id-538 > circle").click()
    # page.locator("#id-510 circle").click()
    page.locator(".flex.border.border-\\[\\#545454\\].border-opacity-75.bg-gradient-to-b > .flex.justify-between > .flex.font-bold > .relative > .text-white.text-2xl").click()
    page.get_by_role("img", name="Material SC Risk, 0.5.").click()
    page.get_by_role("img", name="Order Size, 0.1. Negative").click()
    page.get_by_role("img", name="SC Geo Risk, 0.4. Negative").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
