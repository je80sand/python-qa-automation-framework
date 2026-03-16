from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config_reader import load_settings


class SearchPage(BasePage):

    SEARCH_INPUT = (By.NAME, "q")

    def __init__(self, driver):
        super().__init__(driver)
        settings = load_settings()
        self.url = "https://www.google.com"

    def open(self):
        self.open_url(self.url)

    def search(self, text):
        self.type(self.SEARCH_INPUT, text)
        self.find(self.SEARCH_INPUT).submit()