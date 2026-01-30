# import re
# from playwright.sync_api import Playwright, sync_playwright, expect
# import time

# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("http://103.204.95.212:8084/")
#     page.get_by_role("textbox", name="Username or email").click()
#     page.get_by_role("textbox", name="Username or email").fill("user@gmail.com")
#     page.get_by_role("textbox", name="Password").click()
#     page.get_by_role("textbox", name="Password").fill("12345")
#     page.get_by_role("button", name="LOGIN").click()
#     page.locator("div").filter(has_text=re.compile(r"^Market Intelligence$")).first.click()
#     page.locator("path:nth-child(4)").first.click()
#     page.get_by_role("img", name="USA, z: 5,114. Data Points.").click()
#     page.get_by_role("img", name="IRL, z: 538. Data Points.").click()
#     page.get_by_role("button", name="Competitor").click()
#     page.get_by_role("checkbox", name="ISG").click()
#     page.get_by_role("button", name="Search").click()
#     page.get_by_role("img", name="IRL, z: 129. Data Points.").click()
#     page.get_by_role("img", name="CHN, z: 57. Data Points.").click()
#     page.get_by_role("combobox").first.select_option("topic_discovery")
#     page.locator(".highcharts-series.highcharts-series-4 > .highcharts-tracker-line").click()
#     page.locator(".flex.items-center.ml-auto > .relative > .text-lg").click()
#     page.get_by_role("combobox").nth(1).select_option("A34SNO")
#     page.locator(".relative.flex > .text-xl").click()
#     page.get_by_role("img", name="Tuesday, 31 Mar 2020, 9.8.").click()
#     page.get_by_role("img", name="Wednesday, 30 Nov 2022, 13.37").click()
#     page.locator(".flex.items-center > button").click()
#     page.locator("form").get_by_role("combobox").select_option("health")
#     page.get_by_role("img", name="Monday, 30 Nov 2020, 11.54.").click()
#     page.get_by_role("img", name="Thursday, 30 Jun 2022, 13.1.").click()
#     with page.expect_popup() as page1_info:
#         page.locator(".flex.items-center.justify-between > .text-lg").click()
#     page1 = page1_info.value
#     page1.goto("http://103.204.95.212:8084/market_indicator")
#     page1 = page1_info.value
#     time.sleep(2)
#     chart = page1.locator(".highcharts-container svg")

#     chart.hover(position={"x": 350, "y": 220})
#     page1.wait_for_timeout(200)

#     print(page1.locator(".highcharts-tooltip").inner_text())

#     time.sleep(2)
#     page1.locator(".highcharts-markers.highcharts-series-0.highcharts-line-series.highcharts-tracker.highcharts-series-hover > .highcharts-halo").click()

#     time.sleep(2)
#     page1.locator(".highcharts-point.highcharts-internal-node-interactive.highcharts-point-hover").click()
#     page1.locator(".highcharts-series.highcharts-series-0.highcharts-line-series.highcharts-series-hover > .highcharts-tracker-line").click()
#     page1.get_by_text("Created with Highcharts 11.4.8Growth RateIndexFinanceJan 2018Jan 2019Jan").click()
#     page1.locator(".highcharts-markers.highcharts-series-0.highcharts-line-series.highcharts-tracker.highcharts-series-hover > .highcharts-halo").click()
#     page1.locator(".highcharts-series.highcharts-series-0.highcharts-line-series.highcharts-series-hover > .highcharts-tracker-line").click()
#     page1.locator(".highcharts-series.highcharts-series-0.highcharts-line-series.highcharts-series-hover > .highcharts-tracker-line").click()
#     page1.locator(".highcharts-series.highcharts-series-0.highcharts-line-series.highcharts-series-hover > .highcharts-tracker-line").click()
#     page1.locator(".highcharts-series.highcharts-series-0.highcharts-line-series.highcharts-series-hover > .highcharts-tracker-line").click()
#     page1.locator(".highcharts-series.highcharts-series-0.highcharts-line-series.highcharts-series-hover > .highcharts-tracker-line").click()
#     page1.get_by_role("button", name="listIcon").click()
#     page1.get_by_role("textbox").first.fill("2016-01-19")
#     page1.get_by_role("textbox").nth(1).fill("2026-01-13")
#     page1.get_by_role("button", name="Search").click()
#     page1.get_by_role("button", name="Next", exact=True).click()
#     page1.locator(".highcharts-series.highcharts-series-0.highcharts-line-series.highcharts-series-hover > .highcharts-tracker-line").click()
#     page1.locator(".highcharts-series.highcharts-series-0.highcharts-line-series.highcharts-series-hover > .highcharts-tracker-line").click()
#     page1.get_by_role("img", name="01-01-2021, 91.268. Internet").click()
#     page1.get_by_role("img", name="31-10-2018, 6,067. Asset-").click()
#     page1.get_by_role("img", name="30-09-2019, 2,018.987613.").click()
#     page.get_by_role("img", name="HomeMenu").click()
#     page.locator("div").filter(has_text=re.compile(r"^Demand Intelligence$")).first.click()

#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
import re
import time
from core.navigation import open_market_intelligence
from core.actions import step_click, step_select, step_fill, logger
from core.actions import wait_for_api



def run(page):
    """
    Market Intelligence – Demand Insights
    Uses existing framework:
    - single browser
    - single login
    - step-based logging
    """

    logger.info("📊 Market Intelligence started")

    # ================= OPEN TILE =================
    # 1️⃣ Click the tile first
    open_market_intelligence(page)
# Wait for slow backend API (SYNC SAFE)
    with page.expect_response(
        lambda r: "analyze_topics" in r.url and r.status == 200,
        timeout=120000
    ):
        pass

    # Wait for chart render
    page.wait_for_selector(
        "svg.highcharts-root path.highcharts-point",
        timeout=30000
    )

    # ================= MAP INTERACTIONS =================
    step_click(
    page.get_by_role("img", name=re.compile(r"USA, z:")),
    "USA data point"
)


    step_click(
        page.get_by_role("img", name="IRL, z: 538. Data Points."),
        "IRL data point"
    )

    # ================= COMPETITOR FILTER =================
    step_click(
        page.get_by_role("button", name="Competitor"),
        "Competitor filter"
    )

    step_click(
        page.get_by_role("checkbox", name="ISG"),
        "ISG competitor checkbox"
    )

    step_click(
        page.get_by_role("button", name="Search"),
        "Search competitor"
    )

    step_click(
    page.get_by_role("img", name=re.compile(r"IRL, z:")),
    "IRL data point"
)


    step_click(
    page.get_by_role("img", name=re.compile(r"CHN, z:")),
    "CHN data point"
)


    # ================= CHART INTERACTION =================
    step_select(
        page.get_by_role("combobox").first,
        "topic_discovery",
        "Topic discovery dropdown"
    )

    # step_click(
    #     page.locator(".highcharts-series.highcharts-series-4 > .highcharts-tracker-line"),
    #     "Topic discovery chart line"
    # )

    step_click(
        page.locator(".flex.items-center.ml-auto > .relative > .text-lg"),
        "Chart expand"
    )

    step_select(
        page.get_by_role("combobox").nth(1),
        "A34SNO",
        "Indicator dropdown"
    )

    step_click(
        page.locator(".relative.flex > .text-xl"),
        "Indicator expand"
    )

    # ================= DATE SELECTION =================
    step_click(
        page.get_by_role("img", name="Tuesday, 31 Mar 2020, 9.8."),
        "Date point Mar 2020"
    )

    step_click(
        page.get_by_role("img", name="Wednesday, 30 Nov 2022, 13.37"),
        "Date point Nov 2022"
    )

    step_click(
        page.locator(".flex.items-center > button"),
        "Apply date filter"
    )

    step_select(
        page.locator("form").get_by_role("combobox"),
        "health",
        "Sector dropdown"
    )

    step_click(
        page.get_by_role("img", name="Monday, 30 Nov 2020, 11.54."),
        "Date Nov 2020"
    )

    step_click(
        page.get_by_role("img", name="Thursday, 30 Jun 2022, 13.1."),
        "Date Jun 2022"
    )

    # ================= MARKET INDICATOR POPUP =================
    with page.expect_popup() as popup_info:
        step_click(
            page.locator(".flex.items-center.justify-between > .text-lg"),
            "Open market indicator popup"
        )

    popup = popup_info.value
    popup.wait_for_load_state("domcontentloaded")
    logger.info("📊 Market Indicator popup opened")

    # Wait for SVG controls to be ready
    popup.wait_for_selector("svg.cursor-pointer", timeout=15000)

    # ================= POPUP TAB INTERACTIONS =================
    popup.locator(
        "div:nth-child(4) .graph-heading svg.cursor-pointer"
    ).first.click(force=True)
    time.sleep(1)

    popup.locator(
        "div:nth-child(5) .graph-heading svg.cursor-pointer"
    ).first.click(force=True)
    time.sleep(1)

    # popup.get_by_text("GS: 932", exact=True).click()
    time.sleep(1)

    popup.locator(
        "div:nth-child(6) .graph-heading svg.cursor-pointer"
    ).first.click(force=True)
    time.sleep(1)

    popup.get_by_role(
        "img",
        name="-07-2022, 2.671. Commercial."
    ).click()
    time.sleep(1)

    # ================= CLOSE POPUP (LAST STEP) =================
    popup.locator("svg.cursor-pointer").last.click(force=True)
    logger.info("❌ Market Indicator popup closed")

    popup.close()

    # ================= RETURN HOME =================
    step_click(
        page.get_by_role("img", name="HomeMenu"),
        "Home menu"
    )

   

    logger.info("✅ Market Intelligence completed")

    
