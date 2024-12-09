import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
import time
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage  # LoginPage inherits from BasePage and contains admin_login
import config

class TestDashboard(unittest.TestCase):
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

    def test_send_money_button(self):

        login_page = LoginPage(self.driver)
        login_page.admin_login()

        dashboard_page = DashboardPage(self.driver)
        dashboard_page.load()
        time.sleep(10)

