# import re
# import time
# from playwright.sync_api import Playwright, sync_playwright, expect


# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("http://103.204.95.212:8084//")
#     page.get_by_role("textbox", name="Username or email").click()
#     page.get_by_role("textbox", name="Username or email").fill("user@gmail.com")
#     page.get_by_role("textbox", name="Password").click()
#     page.get_by_role("textbox", name="Password").fill("12345")
#     page.get_by_role("checkbox", name="Remember Me").check()
#     page.get_by_role("button", name="LOGIN").click()
#     page.get_by_role("img", name="Report").click()
#     page.get_by_role("button", name="Go").click()

#     page.wait_for_timeout(1000)
#     page.mouse.wheel(0, 1500)

#     # page.locator("path").nth(4).click()
#     page.get_by_role("button", name="Identified Trends").click()
#     time.sleep(1)
#     page.get_by_role("button", name="Emerging Business").click()
#     time.sleep(1)
#     page.get_by_role("button", name="Strategic Recommendations").click()
#     time.sleep(1)
#     page.get_by_role("button", name="Turning Points And Timeline").click()
#     time.sleep(1)
#     page.get_by_role("button", name="Quantitative Forecasts And").click()
#     time.sleep(1)
#     page.get_by_role("img", name="3, 500. Microsoft Mount").click()
#     page.locator("rect").nth(2).click()
#     page.get_by_role("img", name="2, 100. Great Lakes Data").click()
#     page.get_by_role("img", name="3, 77. Great Lakes Data").click()
#     page.get_by_role("img", name="1, 224. Great Lakes Data").click()
#     page.get_by_role("button", name="Conclusion").click()
#     time.sleep(1)
#     page.get_by_role("img").first.click()
#     page.get_by_role("img", name="Report").click()
#     time.sleep(1)
#     page.get_by_role("combobox").select_option("nuclear")
#     time.sleep(1)
#     page.get_by_role("button", name="Go").click()
#     page.wait_for_timeout(1000)
#     page.mouse.wheel(0, 1500)
#     # page.get_by_role("img").nth(5).click()
#     page.get_by_text("Identified Regulatory RisksJanuary 19-25, 2026: China competitive pressure").click()
#     page.get_by_role("button", name="Key US Nuclear Policies").click()
#     page.get_by_role("button", name="Quantitative Forecasts And").click()
#     page.get_by_role("img", name="4, 2,728. DOE Uranium").click()
#     page.get_by_role("img", name="2, 900. DOE Uranium").click()
#     page.get_by_role("img", name="1, 900. DOE Uranium").click()
#     page.get_by_role("button", name="Strategic Opportunities For").click()
#     page.get_by_role("button", name="Strategic Recommendations").click()
#     page.get_by_role("button", name="Conclusion").click()
#     page.locator("#frequency").select_option("monthly")
#     # page.get_by_role("img").nth(5).click()
#     page.wait_for_timeout(1000)
#     page.mouse.wheel(0, 1500)
#     page.get_by_role("img", name="3, 2. December 2025 Nuclear-").click()
#     time.sleep(1)
#     page.get_by_role("button", name="Strategic Opportunities For").click()
#     time.sleep(1)
#     page.get_by_role("button", name="Strategic Recommendations").click()
#     time.sleep(1)
#     page.get_by_role("button", name="Conclusion").click()

#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
import time
from core.navigation import open_reports, go_back
from core.actions import step_click, step_select, logger


def run(page):
    """
    Reports – Demand Insights (5th micro card)
    Minimal-change refactor
    """

    logger.info("📑 Reports started")

    # ---------------- OPEN TILE ----------------
    open_reports(page)

    step_click(
        page.get_by_role("button", name="Go"),
        "Go button"
    )

    page.wait_for_timeout(1000)
    page.mouse.wheel(0, 1500)

    # ---------------- SECTION NAVIGATION ----------------
    step_click(page.get_by_role("button", name="Identified Trends"), "Identified Trends")
    time.sleep(1)

    step_click(page.get_by_role("button", name="Emerging Business"), "Emerging Business")
    time.sleep(1)

    step_click(
        page.get_by_role("button", name="Strategic Recommendations"),
        "Strategic Recommendations"
    )
    time.sleep(1)

    step_click(
        page.get_by_role("button", name="Turning Points And Timeline"),
        "Turning Points And Timeline"
    )
    time.sleep(1)

    step_click(
        page.get_by_role("button", name="Quantitative Forecasts And"),
        "Quantitative Forecasts"
    )
    time.sleep(1)

    # ---------------- DATA POINTS ----------------
    step_click(
        page.get_by_role("img", name="3, 500. Microsoft Mount"),
        "Microsoft Mount data"
    )

    step_click(
        page.locator("rect").nth(2),
        "Chart rect interaction"
    )

    step_click(
        page.get_by_role("img", name="2, 100. Great Lakes Data"),
        "Great Lakes data 1"
    )

    step_click(
        page.get_by_role("img", name="3, 77. Great Lakes Data"),
        "Great Lakes data 2"
    )

    step_click(
        page.get_by_role("img", name="1, 224. Great Lakes Data"),
        "Great Lakes data 3"
    )

    step_click(
        page.get_by_role("button", name="Conclusion"),
        "Conclusion"
    )
    time.sleep(1)

    # ---------------- FILTER CHANGE ----------------
    step_click(page.get_by_role("img").first, "Back to report list")

    step_click(
        page.get_by_role("img", name="Report"),
        "Report icon"
    )

    step_select(
        page.get_by_role("combobox"),
        "nuclear",
        "Energy type dropdown"
    )

    step_click(
        page.get_by_role("button", name="Go"),
        "Go nuclear report"
    )

    page.wait_for_timeout(1000)
    page.mouse.wheel(0, 1500)

    # ---------------- NUCLEAR REPORT ----------------
    step_click(
        page.get_by_text(
            "Identified Regulatory RisksJanuary 19-25, 2026: China competitive pressure"
        ),
        "Identified Regulatory Risks"
    )

    step_click(
        page.get_by_role("button", name="Key US Nuclear Policies"),
        "Key US Nuclear Policies"
    )

    step_click(
        page.get_by_role("button", name="Quantitative Forecasts And"),
        "Quantitative Forecasts"
    )

    step_click(
        page.get_by_role("img", name="4, 2,728. DOE Uranium"),
        "DOE Uranium data 1"
    )

    step_click(
        page.get_by_role("img", name="2, 900. DOE Uranium"),
        "DOE Uranium data 2"
    )

    step_click(
        page.get_by_role("img", name="1, 900. DOE Uranium"),
        "DOE Uranium data 3"
    )

    step_click(
        page.get_by_role("button", name="Strategic Opportunities For"),
        "Strategic Opportunities"
    )

    step_click(
        page.get_by_role("button", name="Strategic Recommendations"),
        "Strategic Recommendations"
    )

    step_click(
        page.get_by_role("button", name="Conclusion"),
        "Conclusion"
    )

    # ---------------- FREQUENCY CHANGE ----------------
    step_select(
        page.locator("#frequency"),
        "monthly",
        "Frequency dropdown"
    )

    page.wait_for_timeout(1000)
    page.mouse.wheel(0, 1500)

    step_click(
        page.get_by_role("img", name="3, 2. December 2025 Nuclear-"),
        "December 2025 Nuclear data"
    )

    time.sleep(1)

    step_click(
        page.get_by_role("button", name="Strategic Opportunities For"),
        "Strategic Opportunities"
    )
    time.sleep(1)

    step_click(
        page.get_by_role("button", name="Strategic Recommendations"),
        "Strategic Recommendations"
    )
    time.sleep(1)

    step_click(
        page.get_by_role("button", name="Conclusion"),
        "Conclusion"
    )

    # ---------------- BACK ----------------
    go_back(page)

    logger.info("✅ Reports completed")
