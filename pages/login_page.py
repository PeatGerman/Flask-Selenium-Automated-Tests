from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import config

class LoginPage(BasePage):
    URL = config.LOGIN_URL

    def __init__(self, driver):
        super().__init__(driver)
        self.error_message = (By.CSS_SELECTOR, "div#error-message-container p")

    def load(self):
        self.driver.get(self.URL)

    def get_error_message(self):
        return self.wait_for_element(self.error_message).text
