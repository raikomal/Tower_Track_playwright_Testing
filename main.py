from core.browser import get_page, close_browser
from core.login import login
from core.navigation import (
    go_to_demand_insights,
    open_demand_intelligence,
    # go_to_capacity_insights,
    # go_to_supply_insights
)

from core.actions import save_csv


# ===== DEMAND INSIGHTS =====
from sliders.demand.market import run as market_intel
from sliders.demand.demand import run as demand_intel
from sliders.demand.Procurement import run as procurement
from sliders.demand.Pricing import run as pricing
from sliders.demand.reports import run as demand_report


# ===== CAPACITY INSIGHTS =====
# from sliders.capacity.capacity_depletion import run as capacity_depletion

# ===== SUPPLY INSIGHTS =====
# from sliders.supply.supply_intelligence import run as supply_intel
# from sliders.supply.supply_risk import run as supply_risk


def main():
    page = get_page()

    try:
        login(page)

        # DEMAND
        go_to_demand_insights(page)

        market_intel(page)

        open_demand_intelligence(page)   # ✅ ONLY HERE
        demand_intel(page)

        procurement(page)
        pricing(page)
        demand_report(page)

        # # CAPACITY
        # go_to_capacity_insights(page)
        # capacity_depletion(page)

        # # SUPPLY
        # go_to_supply_insights(page)
        # supply_intel(page)
        # supply_risk(page)

    finally:
        # ✅ ALWAYS EXECUTES (PASS / FAIL / CRASH)
        save_csv()
        close_browser()

if __name__ == "__main__":
    main()
