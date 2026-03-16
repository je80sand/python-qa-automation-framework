from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.config_reader import load_settings
from utils.logger import get_logger


logger = get_logger("driver_factory")


def get_driver():
    settings = load_settings()

    browser = settings["browser"].lower()
    headless = settings["headless"]
    window_width = settings["window_width"]
    window_height = settings["window_height"]

    if browser != "chrome":
        raise ValueError(f"Unsupported browser: {browser}")

    options = webdriver.ChromeOptions()

    if headless:
        options.add_argument("--headless=new")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument(f"--window-size={window_width},{window_height}")

    logger.info("Starting Chrome WebDriver")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.implicitly_wait(5)
    return driver