import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
import config


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = EdgeOptions()
        options.use_chromium = True
        driver_path = 'msedgedriver.exe'
        service = EdgeService(executable_path=driver_path)
        cls.driver = webdriver.Edge(service=service, options=options)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_valid_admin_login(self):
        login_page = LoginPage(self.driver)
        login_page.load()
        login_page.login(config.VALID_ADMIN_USERNAME, config.VALID_ADMIN_PASSWORD)
        WebDriverWait(self.driver, 10).until(EC.url_changes(config.LOGIN_URL))
        current_url = self.driver.current_url
        login_page.logout()

        self.assertIn('src/admin/', current_url, "Die URL sollte 'src/admin/' enthalten.")

    def test_valid_user_login(self):
        login_page = LoginPage(self.driver)
        login_page.load()
        login_page.login(config.VALID_USER_USERNAME, config.VALID_USER_PASSWORD)
        WebDriverWait(self.driver, 10).until(EC.url_changes(config.LOGIN_URL))
        current_url = self.driver.current_url
        login_page.logout()

        self.assertIn('src/user/', current_url, "Die URL sollte 'src/user/' enthalten.")

    def test_empty_username_and_password(self):
        login_page = LoginPage(self.driver)
        login_page.load()
        login_page.login("", "")
        error_message = login_page.get_error_message()
        expected_message = config.ERROR_MESSAGES["empty_username_password"]
        self.assertEqual(error_message, expected_message)

    def test_empty_username(self):
        login_page = LoginPage(self.driver)
        login_page.load()
        login_page.login("", config.VALID_USER_PASSWORD)
        error_message = login_page.get_error_message()
        expected_message = config.ERROR_MESSAGES["empty_username_password"]
        self.assertEqual(error_message, expected_message)

    def test_empty_password(self):
        login_page = LoginPage(self.driver)

