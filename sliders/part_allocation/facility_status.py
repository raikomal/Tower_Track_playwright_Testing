# import re
# import time
# from playwright.sync_api import sync_playwright


# def run():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(
#             headless=False,
#             args=["--start-maximized"]
#         )

#         context = browser.new_context(no_viewport=True)
#         page = context.new_page()

#         # ---------------- OPEN APP ----------------
#         page.goto("http://103.204.95.212:8084/", wait_until="domcontentloaded")
#         page.wait_for_load_state("networkidle")

#         # ---------------- LOGIN ----------------
#         page.get_by_role("textbox", name="Username or email").fill("user@gmail.com")
#         page.get_by_role("textbox", name="Password").fill("12345")
#         page.get_by_role("checkbox", name="Remember Me").check()
#         page.get_by_role("button", name="LOGIN").click()

#         page.wait_for_load_state("networkidle")
#         time.sleep(1)

#         # ---------------- OPTIONAL ZOOM OUT (UI FIX) ----------------
#         for _ in range(4):
#             page.keyboard.press("ControlOrMeta+-")
#             time.sleep(0.3)

#         # ---------------- NAVIGATION ----------------
#         page.get_by_role("button", name="Part Allocation Insights").click()
#         time.sleep(1)

#         page.get_by_role("img", name="Facility Status Tracker").click()
#         page.wait_for_load_state("networkidle")
#         time.sleep(1)

#         # ---------------- FACILITY MAP CLICKS ----------------
#         page.get_by_role("img", name=re.compile(r"SAT6.*Facilities")).click()
#         page.get_by_role("img", name=re.compile(r"NVA9.*Facilities")).click()
#         page.get_by_role("img", name=re.compile(r"LON6.*Facilities")).click()
#         page.get_by_role("img", name=re.compile(r"MIL1.*Facilities")).click()
#         page.get_by_role("img", name=re.compile(r"OSK1.*Facilities")).click()

#         # ---------------- TABLE FILTER CLICKS ----------------
#         page.get_by_role("cell", name="%").nth(1).click()
#         page.get_by_role("cell", name="PHX2").click()
#         page.get_by_role("cell", name="PHX1").click()
#         page.get_by_role("cell", name="89%").first.click()

#         # ---------------- DROPDOWNS ----------------
#         page.get_by_role("combobox").first.select_option("barchart")

#         page.get_by_role("combobox").nth(1).select_option("MAD1 (Madrid, ES)")
#         page.get_by_role("combobox").nth(1).select_option("DUR1 (Durham, NC)")

#         page.get_by_role("combobox").nth(2).select_option("resource")
#         page.get_by_role("combobox").nth(2).select_option("alert")
#         page.get_by_role("combobox").nth(2).select_option("transportation")

#         # ---------------- BAR / ICON INTERACTIONS ----------------
#         page.get_by_role("img", name=re.compile(r"PHX4.*Fulfillment")).click()
#         page.get_by_role("img", name=re.compile(r"PHX6.*Fulfillment")).click()

#         # Scroll chart into view
#         page.locator("svg.highcharts-root").first.scroll_into_view_if_needed()
#         page.wait_for_timeout(500)

#         # Click first 3 bars in the readiness chart (generic but stable)
#         bars = page.locator("svg.highcharts-root rect").filter(has_text="")

#         count = bars.count()
#         if count >= 3:
#            bars.nth(0).click(force=True)
#            bars.nth(1).click(force=True)
#            bars.nth(2).click(force=True)


#         # ---------------- POPUP ----------------
#         with page.expect_popup() as popup_info:
#             page.locator(
#                 ".flex.justify-between.items-center.gap-2 > .pointer-events-auto"
#             ).click()

#         popup = popup_info.value
#         popup.wait_for_load_state("networkidle")
#         time.sleep(1)

#         popup.get_by_role("combobox").first.select_option("PHX1")
#         popup.get_by_role("combobox").nth(1).select_option("Phase B")

#         # ---------------- END ----------------
#         print("✅ Facility Status Tracker automation completed")

#         context.close()
#         browser.close()


# if __name__ == "__main__":
#     run()
