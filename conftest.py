import pytest
from utils.driver_factory import get_driver
from utils.logger import get_logger
from utils.screenshot_helper import save_screenshot


logger = get_logger("conftest")


@pytest.fixture
def driver():
    logger.info("Creating test driver")
    driver = get_driver()
    yield driver
    logger.info("Quitting test driver")
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot_path = save_screenshot(driver, item.name)
            logger.error(f"Test failed: {item.name}")
            logger.error(f"Screenshot saved: {screenshot_path}")