
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import config

class LoginPage:
    URL = config.LOGIN_URL

    def __init__(self, driver: WebDriver):
        self.driver = driver


        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.error_message = (By.CSS_SELECTOR, "div.error")
        self.logout_button = (By.ID, "logout_button")

    def load(self):
        self.driver.get(self.URL)

    def enter_username(self, username: str):
        username_field = self.driver.find_element(*self.username_input)
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password: str):
        password_field = self.driver.find_element(*self.password_input)
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def logout(self):
        self.driver.find_element(*self.logout_button).click()