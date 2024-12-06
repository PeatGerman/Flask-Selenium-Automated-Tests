from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

import config


class BasePage:


    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.logout_button = (By.ID, "logout_button")

    def wait_for_element(self, locator: tuple, timeout=10):

        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_and_click(self, locator: tuple, timeout=10):

        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def enter_text(self, locator: tuple, text: str, timeout=10):

        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def admin_login(self):
        login_page = self.driver
        self.load()
        self.login(config.VALID_ADMIN_USERNAME, config.VALID_ADMIN_PASSWORD)
        WebDriverWait(self.driver, 10).until(EC.url_changes(config.LOGIN_URL))
        current_url = self.driver.current_url

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def logout(self):
        self.wait_and_click(self.logout_button)