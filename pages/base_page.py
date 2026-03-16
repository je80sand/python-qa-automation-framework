from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config_reader import load_settings
from utils.logger import get_logger


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        settings = load_settings()
        self.wait = WebDriverWait(driver, settings["timeout"])
        self.logger = get_logger(self.__class__.__name__)

    def open_url(self, url):
        self.logger.info(f"Opening URL: {url}")
        self.driver.get(url)

    def find(self, locator):
        self.logger.info(f"Finding element: {locator}")
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        self.logger.info(f"Clicking element: {locator}")
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def type(self, locator, text):
        self.logger.info(f"Typing into element: {locator} with text: {text}")
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        self.logger.info(f"Getting text from element: {locator}")
        return self.find(locator).text