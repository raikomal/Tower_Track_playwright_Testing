# import re
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
#     page.locator("div").nth(3).click()
#     page.get_by_role("checkbox", name="Remember Me").check()
#     page.get_by_role("button", name="LOGIN").click()
#     page.locator("div").filter(has_text=re.compile(r"^Pricing Optimization$")).first.click()
#     page.get_by_role("img").nth(4).click()
#     page.get_by_role("img", name="x, 350, 45,000. Revenue Curve.").click()
#     page.get_by_role("img", name="x, 300, 60,000. Revenue Curve.").click()
#     page.get_by_role("img", name="x, 250, 70,000. Revenue Curve.").click()
#     page.get_by_role("img", name="x, 150, 60,000. Revenue Curve.").click()
#     page.locator("div:nth-child(2) > .flex.items-center.justify-between > .flex.items-center.gap-3 > .relative > .text-white.text-xl").first.click()
#     page.get_by_role("img", name="20%. Price: $300/kW.").click()
#     page.get_by_role("img", name="30%. Price: $300/kW.").click()
#     page.get_by_role("img", name="80%. Price: $300/kW.").click()
#     page.locator("div:nth-child(2) > div > .flex.items-center.justify-between > .flex.items-center.gap-3 > .relative > .text-white.text-xl > path:nth-child(4)").first.click()
#     page.get_by_role("img", name="$17,000,000. Revenue Curve.").click()
#     page.get_by_role("img", name="$15,500,000. Revenue Curve.").click()
#     page.get_by_role("img", name="$13,000,000. Revenue Curve.").click()
#     page.get_by_role("img", name="$11,500,000. Revenue Curve.").click()
#     page.get_by_role("img", name="$10,500,000. Revenue Curve.").click()
#     page.get_by_role("img", name="$10,000,000. Revenue Curve.").click()
#     page.locator("div:nth-child(2) > div:nth-child(2) > .flex.items-center.justify-between > .flex.items-center.gap-3 > .relative > .text-white.text-xl").click()
#     page.get_by_role("img", name="5/19, 300. DLR incl.").click()
#     page.get_by_role("img", name="6/19, 270. DLR incl.").click()
#     page.get_by_role("img", name="/19, 320. DLR incl.").click()
#     page.get_by_role("img", name="/19, 280. DLR incl.").click()
#     page.get_by_role("img", name="/19, 290. DLR incl.").click()
#     page.get_by_role("img", name="2/19, 70. IRM.").click()
#     page.get_by_role("img", name="5/19, 90. IRM.").click()
#     page.get_by_role("img", name="11/19, 90. IRM.").click()
#     page.get_by_role("img", name="5/19, 240. DLR Turnkey.").click()
#     page.get_by_role("img", name="7/19, 260. DLR Turnkey.").click()
#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
from core.navigation import open_pricing, go_back
from core.actions import step_click, logger


def run(page):
    """
    Pricing Optimization – Demand Insights
    Minimal-change refactor
    """

    logger.info("💰 Pricing Optimization started")

    # ---------------- OPEN TILE ----------------
    open_pricing(page)

    # ---------------- PRICE CURVE ----------------
    step_click(page.get_by_role("img").nth(4), "Pricing chart expand")

    step_click(
        page.get_by_role("img", name="x, 350, 45,000. Revenue Curve."),
        "Revenue curve point 45k"
    )

    step_click(
        page.get_by_role("img", name="x, 300, 60,000. Revenue Curve."),
        "Revenue curve point 60k"
    )

    step_click(
        page.get_by_role("img", name="x, 250, 70,000. Revenue Curve."),
        "Revenue curve point 70k"
    )

    step_click(
        page.get_by_role("img", name="x, 150, 60,000. Revenue Curve."),
        "Revenue curve point 60k low"
    )

    # ---------------- PRICE SLIDER ----------------
    step_click(
        page.locator(
            "div:nth-child(2) > .flex.items-center.justify-between > "
            ".flex.items-center.gap-3 > .relative > .text-white.text-xl"
        ).first,
        "Open price slider"
    )

    step_click(
        page.get_by_role("img", name="20%. Price: $300/kW."),
        "20% price point"
    )

    step_click(
        page.get_by_role("img", name="30%. Price: $300/kW."),
        "30% price point"
    )

    step_click(
        page.get_by_role("img", name="80%. Price: $300/kW."),
        "80% price point"
    )

    # ---------------- REVENUE VIEW ----------------
    step_click(
        page.locator(
            "div:nth-child(2) > div > .flex.items-center.justify-between > "
            ".flex.items-center.gap-3 > .relative > .text-white.text-xl > path:nth-child(4)"
        ).first,
        "Switch revenue view"
    )

    # step_click(
    #     page.get_by_role("img", name="$17,000,000. Revenue Curve."),
    #     "Revenue 17M"
    # )

    # step_click(
    #     page.get_by_role("img", name="$15,500,000. Revenue Curve."),
    #     "Revenue 15.5M"
    # )

    step_click(
        page.get_by_role("img", name="$13,000,000. Revenue Curve."),
        "Revenue 13M"
    )

    step_click(
        page.get_by_role("img", name="$11,500,000. Revenue Curve."),
        "Revenue 11.5M"
    )

    step_click(
        page.get_by_role("img", name="$10,500,000. Revenue Curve."),
        "Revenue 10.5M"
    )

    step_click(
        page.get_by_role("img", name="$10,000,000. Revenue Curve."),
        "Revenue 10M"
    )

    # ---------------- COST BREAKDOWN ----------------
    step_click(
        page.locator(
            "div:nth-child(2) > div:nth-child(2) > "
            ".flex.items-center.justify-between > "
            ".flex.items-center.gap-3 > .relative > .text-white.text-xl"
        ),
        "Open cost breakdown"
    )

    step_click(
        page.get_by_role("img", name="5/19, 300. DLR incl."),
        "DLR incl point 1"
    )

    step_click(
        page.get_by_role("img", name="6/19, 270. DLR incl."),
        "DLR incl point 2"
    )

    step_click(
        page.get_by_role("img", name="/19, 320. DLR incl."),
        "DLR incl point 3"
    )

    step_click(
        page.get_by_role("img", name="/19, 280. DLR incl."),
        "DLR incl point 4"
    )

    step_click(
        page.get_by_role("img", name="/19, 290. DLR incl."),
        "DLR incl point 5"
    )

    # ---------------- IRM & TURNKEY ----------------
    step_click(
        page.get_by_role("img", name="2/19, 70. IRM."),
        "IRM point 1"
    )

    step_click(
        page.get_by_role("img", name="5/19, 90. IRM."),
        "IRM point 2"
    )

    step_click(
        page.get_by_role("img", name="11/19, 90. IRM."),
        "IRM point 3"
    )

    step_click(
        page.get_by_role("img", name="5/19, 240. DLR Turnkey."),
        "DLR Turnkey point 1"
    )

    step_click(
        page.get_by_role("img", name="7/19, 260. DLR Turnkey."),
        "DLR Turnkey point 2"
    )

    # ---------------- BACK ----------------
    

    logger.info("✅ Pricing Optimization completed")
    # ---------------- BACK (Pricing specific) ----------------
    step_click(page.locator("//img[@alt='HomeMenu']"),
    "Home menu (exit Pricing)")
    
    
    # wait until dashboard tiles are visible
    page.wait_for_selector("text=Demand Intelligence", timeout=20000)

