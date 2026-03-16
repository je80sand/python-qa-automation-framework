from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config_reader import load_settings


class LoginPage(BasePage):

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")

    def __init__(self, driver):
        super().__init__(driver)
        settings = load_settings()
        self.url = f'{settings["base_url"]}/login'

    def open(self):
        self.open_url(self.url)

    def enter_username(self, username):
        self.type(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.type(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_flash_message(self):
        return self.get_text(self.FLASH_MESSAGE)