from core.browser import get_page, close_browser

from sliders.demand.market import run as demand_market
from sliders.capacity.capacity_depletion import run as capacity_depletion
from sliders.supply.supply_intelligence import run as supply_intel


def main():
    page = get_page()

    demand_market(page)
    capacity_depletion(page)
    supply_intel(page)

    close_browser()


if __name__ == "__main__":
    main()
