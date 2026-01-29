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
    page.get_by_role("checkbox", name="Remember Me").check()
    page.get_by_role("button", name="LOGIN").click()
    page.get_by_role("img", name="Market Intelligence").click()
    with page.expect_popup() as page1_info:
        page.locator(".flex.items-center.justify-between > .text-lg").click()
    page1 = page1_info.value
    page1.locator("path").nth(4).click()
    # page1.get_by_role("heading", name="Producer Price Index: Electronics Producer Price Index: Telecommunication").locator("svg").click()
    page1.locator("div:nth-child(4) > .graph-heading > .flex.items-center.justify-between > .relative > .text-white.text-lg").click()
    page1.locator("div:nth-child(5) > .graph-heading > .flex.items-center.justify-between > .relative > .text-white.text-lg > path:nth-child(2)").click()
    page1.locator("text").filter(has_text=re.compile(r"^GS: 932$")).click()
    page1.locator("div:nth-child(6) > .graph-heading > .flex.items-center.justify-between > .relative > .text-white.text-lg").click()
    page1.get_by_role("img", name="-07-2022, 2.671. Commercial.").click()
    time.sleep(1)
    page1.locator(".flex.items-center.gap-2 > .relative > .text-white.text-lg").click()
    time.sleep(1)

    page1.locator("path").first.click()
    time.sleep(1)
    page1.close()
    time.sleep(2)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

    #demand intelligence 
#      page.locator("div").filter(has_text=re.compile(r"^Demand Intelligence$")).first.click()
#     page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.001, 1.19. GDP.").click()
#     page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.000, -1.72. GDP.").click()
#     page.locator(".text-white.text-4xl").click()
#     page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(5).click()
#     page.get_by_role("textbox").first.fill("2023-01-02")
#     page.get_by_role("textbox").nth(1).fill("2025-02-27")
#     page.get_by_role("combobox").first.select_option("FEDFUNDS")
#     page.get_by_role("combobox").nth(1).select_option("C2")
#     page.get_by_role("combobox").nth(2).select_option("F2")
#     page.get_by_role("button", name="Search").click()
#     page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.004").click()
#     page.get_by_role("img", name="Thursday, 1 Jan, 00:00:00.003").click()
#     page.locator(".text-xl.mx-2.flex.items-center.justify-center > .relative > .text-white.text-2xl").click()
#     page.locator(".flex-1 > button").click()
#     page.get_by_role("combobox").first.select_option("Health")
#     page.get_by_role("img", name="January 2018, 0. Health.").click()
#     page.get_by_role("img", name="April 2018, 12.5. Health.").nth(1).click()
#     page.get_by_role("img", name="April 2018, 12.5. Health.").nth(1).click()

#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)

