import os
from datetime import datetime


def save_screenshot(driver, test_name):
    os.makedirs("reports/screenshots", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"reports/screenshots/{test_name}_{timestamp}.png"

    driver.save_screenshot(file_path)

    return file_path