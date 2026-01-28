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
    page.get_by_role("button", name="Part Allocation Insights").click()
    time.sleep(2)
    page.get_by_role("img", name="SLA & Risk Heatmap").click()
    time.sleep(2)

    page.locator("section").filter(has_text="SLA & Risk Heatmap").get_by_role("img").click()
    time.sleep(2)

    page.locator("section").filter(has_text="Bottleneck & Dependency").get_by_role("img").click()
    time.sleep(2)

    page.get_by_role("button", name="Operational Insights").click()
    time.sleep(2)

    page.get_by_role("combobox").first.select_option("On-Time, In-Full (OTIF)")
    time.sleep(2)

    page.get_by_role("combobox").nth(1).select_option("HOU4 (Houston, TX)")
    time.sleep(2)

    page.get_by_role("textbox", name="Start Date:").fill("2024-12-04")
    time.sleep(2)

    page.get_by_role("textbox", name="End Date:").fill("2025-07-08")
    time.sleep(2)

    page.get_by_role("button", name="Generate Report").click()
    page.get_by_role("img", name="Interactive chart").click()
    time.sleep(2)

    page.get_by_role("img", name="Interactive chart").click()
    page.get_by_role("img", name="Interactive chart").click()
    time.sleep(2)

    page.locator("section").filter(has_text="SLA & Risk Impact").get_by_role("combobox").select_option("DUR1 (Durham NC)")
    time.sleep(2)

    page.locator("section").filter(has_text="SLA & Risk Impact").get_by_role("combobox").select_option("MAD1 (Madrid)")
    page.get_by_text("SLA & Risk Impact detailsSelect Facility to Query:-- Select Facility to Query").click()
    time.sleep(2)

    page.locator("section").filter(has_text="SLA & Risk Impact").get_by_role("combobox").select_option("DUB1 (Dublin)")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
