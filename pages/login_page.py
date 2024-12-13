from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

import config

class LoginPage(BasePage):
    URL = config.LOGIN_URL

    def __init__(self, driver):
        super().__init__(driver)
        self.error_message = (By.CSS_SELECTOR, "div#error-message-container p")

    def load(self):
        self.driver.get(self.URL)

    def get_error_message(self, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.error_message)
        )
        return element.text