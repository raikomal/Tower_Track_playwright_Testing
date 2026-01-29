from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from core.actions import logger
from core.actions import set_context



def _click_and_wait(page, locator, wait_text=None):
    """
    Common safe click helper
    """
    page.locator(locator).first.click()
    page.wait_for_load_state("networkidle")

    if wait_text:
        page.wait_for_selector(f"text={wait_text}", timeout=15000)


# =======================
# SLIDER NAVIGATION
# =======================

def go_to_demand_insights(page):
    print("➡️ Navigating to Demand Insights")
    set_context(
        application="Demand Insights",
        title="Demand Insights End-to-End Validation"
    )

    # Button / icon based navigation (stable)
    page.get_by_role("button", name="Demand Insights").click()

    # Wait for Market Intelligence tile to confirm page load
    page.wait_for_selector("text=Market Intelligence", timeout=15000)



# def go_to_capacity_insights(page):
#     print("➡️ Navigating to Capacity Insights")
#     page.get_by_role("button", name="Capacity Insights").click()
#     page.wait_for_selector("text=Capacity Depletion", timeout=15000)


# def go_to_supply_insights(page):
#     print("➡️ Navigating to Supply Insights")
#     page.get_by_role("button", name="Supply Insights").click()
#     page.wait_for_selector("text=Supply Intelligence", timeout=15000)

# =======================
# TILE NAVIGATION
# =======================

def open_tile(page, tile_name):
    set_context(micro_application=tile_name)

    """
    Open any dashboard tile by name
    """
    print(f"🔹 Opening tile: {tile_name}")

    _click_and_wait(
        page,
        f"//div[contains(text(),'{tile_name}')]",
        wait_text=tile_name
    )


def go_back(page):
    """
    Universal back button handler
    """
    print("⬅️ Navigating back")

    try:
        page.locator("//button//*[name()='svg']").first.click()
        page.wait_for_load_state("networkidle")
    except PlaywrightTimeoutError:
        raise Exception("❌ Back button not found")


# =======================
# DEMAND TILES (OPTIONAL SHORTCUTS)
# =======================

def open_market_intelligence(page):
    open_tile(page, "Market Intelligence")


def open_demand_intelligence(page):
    logger.info("🔹 Opening tile: Demand Intelligence")

    page.get_by_role("img", name="Demand Intelligence").click()
    page.wait_for_load_state("networkidle")



def open_procurement(page):
    open_tile(page, "Procurement")


def open_pricing(page):
    open_tile(page, "Pricing")


def open_reports(page):
    open_tile(page, "Report")



# # =======================
# # CAPACITY TILES
# # =======================

# def open_capacity_depletion(page):
#     open_tile(page, "Capacity Depletion")


# # =======================
# # SUPPLY TILES
# # =======================

# def open_supply_intelligence(page):
#     open_tile(page, "Supply Intelligence")


# def open_supply_risk(page):
#     open_tile(page, "Supply Risk Assessment")
