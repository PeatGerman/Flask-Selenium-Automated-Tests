import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
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
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.load()
        time.sleep(10)