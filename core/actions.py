import time
import logging
import pandas as pd
from datetime import datetime
import os

# =========================================================
# CONFIG
# =========================================================
STEP_DELAY = 1

# =========================================================
# LOGGER SETUP
# =========================================================
logger = logging.getLogger("playwright_logger")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler("automation.log", mode="a", encoding="utf-8")
file_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

# =========================================================
# TEST CONTEXT
# =========================================================
TEST_CONTEXT = {
    "project": "Hitachi Tower Track",
    "application": "",
    "micro_application": "",
    "title": ""
}

def set_context(application=None, micro_application=None, title=None):
    if application:
        TEST_CONTEXT["application"] = application
    if micro_application:
        TEST_CONTEXT["micro_application"] = micro_application
    if title:
        TEST_CONTEXT["title"] = title


# =========================================================
# TEST DATA STORAGE
# =========================================================
test_data = []

# =========================================================
# RECORD STEP
# =========================================================
def record_step(
    description,
    steps,
    expected_result,
    actual_result,
    status="PASS",
    remarks="",
    comments=""
):
    test_data.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "project": TEST_CONTEXT["project"],
        "application": TEST_CONTEXT["application"],
        "micro_application": TEST_CONTEXT["micro_application"],
        "title": TEST_CONTEXT["title"],
        "description": description,
        "steps": steps,
        "expected_result": expected_result,
        "actual_result": actual_result,
        "status": status,
        "remarks": remarks,
        "comments": comments
    })

# =========================================================
# ACTION WRAPPERS
# =========================================================
def step_click(locator, description):
    try:
        time.sleep(STEP_DELAY)
        logger.info(f"🖱️ CLICK | {description}")
        locator.click()
        record_step(
            description,
            f"Click on {description}",
            f"{description} should be clickable",
            "Clicked successfully"
        )
    except Exception as e:
        logger.error(f"❌ CLICK FAILED | {description} | {e}")
        record_step(
            description,
            f"Click on {description}",
            f"{description} should be clickable",
            str(e),
            "FAIL"
        )
        raise


def step_fill(locator, value, description):
    try:
        time.sleep(STEP_DELAY)
        logger.info(f"⌨️ FILL | {description} = {value}")
        locator.fill(value)
        record_step(
            description,
            f"Enter value in {description}",
            f"{description} should accept input",
            f"Entered value: {value}"
        )
    except Exception as e:
        logger.error(f"❌ FILL FAILED | {description} | {e}")
        record_step(
            description,
            f"Enter value in {description}",
            f"{description} should accept input",
            str(e),
            "FAIL"
        )
        raise


def step_select(locator, value, description):
    try:
        time.sleep(STEP_DELAY)
        logger.info(f"🔽 SELECT | {description} = {value}")
        locator.select_option(value)
        record_step(
            description,
            f"Select {value} from {description}",
            f"{value} should be selectable",
            f"Selected {value}"
        )
    except Exception as e:
        logger.error(f"❌ SELECT FAILED | {description} | {e}")
        record_step(
            description,
            f"Select {value} from {description}",
            f"{value} should be selectable",
            str(e),
            "FAIL"
        )
        raise


def step_press(locator, key, description):
    try:
        time.sleep(STEP_DELAY)
        logger.info(f"⌨️ PRESS | {description} -> {key}")
        locator.press(key)
        record_step(
            description,
            f"Press key {key}",
            "Key press should work",
            f"Pressed {key}"
        )
    except Exception as e:
        logger.error(f"❌ PRESS FAILED | {description} | {e}")
        record_step(
            description,
            f"Press key {key}",
            "Key press should work",
            str(e),
            "FAIL"
        )
        raise

# =========================================================
# SAVE CSV (CALLED ONCE AT END)
# =========================================================
def save_csv():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Ensure directory exists
    output_dir = os.path.join("reports", "final")
    os.makedirs(output_dir, exist_ok=True)

    report_name = f"tower_track_automation_{timestamp}.csv"
    report_path = os.path.join(output_dir, report_name)

    logger.info("📊 Saving CSV report")
    logger.info(f"🧪 Total recorded steps: {len(test_data)}")

    pd.DataFrame(test_data).to_csv(report_path, index=False)

    logger.info(f"✅ Report saved at: {report_path}")


def wait_for_api(page, url_part):
    """
    Safe API wait for SYNC Playwright
    Will NOT break flow if API already fired
    """
    logger.info(f"⏳ Waiting for API: {url_part}")

    try:
        with page.expect_response(
            lambda r: url_part in r.url and r.status in (200, 304),
            timeout=5000
        ):
            pass
    except Exception:
        logger.warning(f"⚠️ API {url_part} already loaded or skipped")
