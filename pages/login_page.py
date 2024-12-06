from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import config

class LoginPage(BasePage):
    URL = config.LOGIN_URL

    def __init__(self, driver):
        super().__init__(driver)  # Konstruktor der Basisklasse aufrufen
        #self.username_input = (By.ID, "username")
        #self.password_input = (By.ID, "password")
        #self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.error_message = (By.CSS_SELECTOR, "div#error-message-container p")


    def load(self):
        self.driver.get(self.URL)

    def enter_username(self, username: str):
        self.enter_text(self.username_input, username)

    def enter_password(self, password: str):
        self.enter_text(self.password_input, password)

    def click_login(self):
        self.wait_and_click(self.login_button)

    def get_error_message(self):
        return self.wait_for_element(self.error_message).text




