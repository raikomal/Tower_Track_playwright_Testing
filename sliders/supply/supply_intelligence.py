# # import re
# # from playwright.sync_api import Playwright, sync_playwright, expect
# # import time

# # def run(playwright: Playwright) -> None:
# #     browser = playwright.chromium.launch(headless=False)
# #     context = browser.new_context()
# #     page = context.new_page()
# #     page.goto("http://103.204.95.212:8084/")
# #     page.get_by_role("textbox", name="Username or email").click()
# #     page.get_by_role("textbox", name="Username or email").fill("user@gmail.com")
# #     page.get_by_role("textbox", name="Password").click()
# #     page.get_by_role("textbox", name="Password").fill("12345")
# #     page.get_by_role("button", name="LOGIN").click()
# #     page.get_by_role("button", name="Supply Insights").click()
# #     page.locator("div").filter(has_text=re.compile(r"^Supply Intelligence$")).first.click()
# #     page.locator("div:nth-child(16)").click()
# #     page.locator("div:nth-child(7)").first.click()
# #     page.locator(".text-white.text-2xl").first.click()
# #     page.get_by_role("combobox").select_option("PieChart")
# #     page.get_by_role("img", name="32,000. Customer.").click()
# #     page.get_by_role("img", name="113,075. Customer.").click()
# #     page.get_by_role("combobox").nth(1).select_option("Facility")
# #     page.get_by_role("img", name="DUR2, 9,000. Facility.").click()
# #     page.get_by_role("img", name="DFW3, 31,607. Facility.").click()
# #     page.get_by_role("img", name="PNW1, 27,000. Facility.").click()
# #     page.get_by_role("combobox").first.select_option("BarChart")
# #     page.locator("rect").nth(2).click()
# #     page.locator("rect").nth(2).click()
# #     page.get_by_role("combobox").select_option("FacilityAllocation")
# #     page.get_by_role("combobox").select_option("")
# #     page.get_by_role("columnheader", name="Customer").locator("button").click()
# #     page.get_by_role("checkbox", name="1", exact=True).check()
# #     page.get_by_role("columnheader", name="Facility", exact=True).locator("button").click()
# #     page.get_by_role("checkbox", name="AMS1").check()
# #     page.get_by_role("checkbox", name="AMS1").uncheck()
# #     page.get_by_role("cell", name="9000 KW").click()
# #     page.locator(".py-2 > button").first.click()
# #     time.sleep(2)
# #     page.get_by_role("textbox").click()
# #     time.sleep(2)
# #     page.get_by_role("textbox").fill("8")
# #     time.sleep(2)
# #     page.get_by_role("button", name="Update").click()
# #     time.sleep(2)
# #     # page.get_by_role("button", name="The graph provides an").click()
# #     # page.get_by_role("img", name="July 2024, 0.49. Historical.").click()
# #     # page.locator(".highcharts-halo").click()

# #        # ---------------------
# #     context.close()
# #     browser.close()


# # # ✅ ENTRY POINT (MUST BE OUTSIDE run)
# # if __name__ == "__main__":
# #     with sync_playwright() as playwright:
# #         run(playwright)
# import time
# import re
# from core.navigation import open_supply_intelligence, go_back
# from core.actions import step_click, step_fill, step_select, logger


# def run(page):
#     """
#     Supply Intelligence – Supply Insights
#     Minimal-change refactor
#     """

#     logger.info("🚚 Supply Intelligence started")

#     # ---------------- OPEN TILE ----------------
#     open_supply_intelligence(page)

#     # ---------------- VIEW / FILTER ----------------
#     step_click(
#         page.locator("div:nth-child(16)"),
#         "Supply intelligence view toggle"
#     )

#     step_click(
#         page.locator("div:nth-child(7)").first,
#         "Supply intelligence sub-section"
#     )

#     step_click(
#         page.locator(".text-white.text-2xl").first,
#         "Open chart controls"
#     )

#     # ---------------- CHART TYPE ----------------
#     step_select(
#         page.get_by_role("combobox"),
#         "PieChart",
#         "Chart type dropdown"
#     )

#     step_click(
#         page.get_by_role("img", name="32,000. Customer."),
#         "Customer 32,000"
#     )

#     step_click(
#         page.get_by_role("img", name="113,075. Customer."),
#         "Customer 113,075"
#     )

#     # ---------------- FACILITY VIEW ----------------
#     step_select(
#         page.get_by_role("combobox").nth(1),
#         "Facility",
#         "View by Facility"
#     )

#     step_click(
#         page.get_by_role("img", name="DUR2, 9,000. Facility."),
#         "DUR2 facility"
#     )

#     step_click(
#         page.get_by_role("img", name="DFW3, 31,607. Facility."),
#         "DFW3 facility"
#     )

#     step_click(
#         page.get_by_role("img", name="PNW1, 27,000. Facility."),
#         "PNW1 facility"
#     )

#     # ---------------- BAR CHART ----------------
#     step_select(
#         page.get_by_role("combobox").first,
#         "BarChart",
#         "Bar chart view"
#     )

#     step_click(
#         page.locator("rect").nth(2),
#         "Bar chart selection"
#     )

#     step_click(
#         page.locator("rect").nth(2),
#         "Bar chart selection repeat"
#     )

#     # ---------------- TABLE VIEW ----------------
#     step_select(
#         page.get_by_role("combobox"),
#         "FacilityAllocation",
#         "Facility allocation view"
#     )

#     # NOTE: empty select kept as-is from your file
#     step_select(
#         page.get_by_role("combobox"),
#         "",
#         "Reset allocation filter"
#     )

#     # ---------------- TABLE FILTERS ----------------
#     step_click(
#         page.get_by_role("columnheader", name="Customer")
#         .locator("button"),
#         "Customer column filter"
#     )

#     step_click(
#         page.get_by_role("checkbox", name="1", exact=True),
#         "Customer filter 1"
#     )

#     step_click(
#         page.get_by_role("columnheader", name="Facility", exact=True)
#         .locator("button"),
#         "Facility column filter"
#     )

#     step_click(
#         page.get_by_role("checkbox", name="AMS1"),
#         "AMS1 facility select"
#     )

#     step_click(
#         page.get_by_role("checkbox", name="AMS1"),
#         "AMS1 facility unselect"
#     )

#     # ---------------- ALLOCATION UPDATE ----------------
#     step_click(
#         page.get_by_role("cell", name="9000 KW"),
#         "9000 KW allocation cell"
#     )

#     step_click(
#         page.locator(".py-2 > button").first,
#         "Edit allocation"
#     )

#     time.sleep(2)

#     step_fill(
#         page.get_by_role("textbox"),
#         "8",
#         "Update allocation value"
#     )

#     step_click(
#         page.get_by_role("button", name="Update"),
#         "Update allocation"
#     )

#     time.sleep(2)

#     # ---------------- BACK ----------------
#     go_back(page)

#     logger.info("✅ Supply Intelligence completed")
