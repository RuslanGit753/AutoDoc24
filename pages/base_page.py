from utils.config import Config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, get_chrome):
        self.driver = get_chrome
        self.BASE_URL = Config.BASE_URL

    def open(self, BASE_URL):
        self.driver.get(BASE_URL)

    def find(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
