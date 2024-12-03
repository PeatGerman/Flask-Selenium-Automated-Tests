from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config


class LoginPage:
    URL = config.LOGIN_URL

    def __init__(self, driver: WebDriver):
        self.driver = driver

        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.error_message = (By.CSS_SELECTOR, "div#error-message-container p")
        self.logout_button = (By.ID, "logout_button")

    def load(self):
        self.driver.get(self.URL)

    def enter_username(self, username: str):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_input)
        )
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password: str):
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password_input)
        )
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        )
        login_button.click()

    def get_error_message(self):
        error_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.error_message)
        )
        return error_element.text

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def logout(self):
        logout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.logout_button)
        )
        logout_button.click()
