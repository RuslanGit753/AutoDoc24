import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    def wait_for_url(self, pattern: str, timeout=10) -> None:
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(pattern))
        
    def clear_cookies(self):
        self.driver.delete_all_cookies()

    def load_user_cookies(self, user_number):
        cookies_file = os.path.join('cookies', f'user{user_number}.json')
        if os.path.exists(cookies_file):
            with open(cookies_file, 'r') as file:
                cookies = json.load(file)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)

    def load_user1_cookies(self):
        self.load_user_cookies(1)

    def load_user2_cookies(self):
        self.load_user_cookies(2)
