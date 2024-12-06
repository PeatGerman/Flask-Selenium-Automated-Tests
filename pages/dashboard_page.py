from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import config


class DashboardPage:
    URL = config.DASHBOARD_URL

    def __init__(self, driver: WebDriver):
        self.driver = driver


        self.send_money_button = (By.XPATH, "//button[contains(@onclick, 'transfer_money.php')]")


    def load(self):
        self.driver.get(self.URL)

    def send_money_button(self):
        self.admin_login()
        send_money_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.send_money_button)
        )
        send_money_button.click()

