import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    """Метод для открытия веб страницы"""
    def open(self, url):
        self.driver.get(url)

    """Ожидание локатора элемента"""
    def find(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    """Ожидание пока элемент не станет кликабельным"""
    def find_elem_click(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))

    """Ожидание появления нескольких элементов"""
    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator))

    """Ожидание появления необходимого URL"""
    def wait_for_url(self, pattern: str, timeout=10) -> None:
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(pattern))

    """Прокрутка страницы до необходимого элемента"""
    def scrol_page(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});",
            element)

    """Очистка кук"""
    def clear_cookies(self):
        self.driver.delete_all_cookies()

    """Загрузка кук на страницу"""
    def load_user_cookies(self, user_number):
        cookies_file = os.path.join('cookies', f'user{user_number}.json')
        if os.path.exists(cookies_file):
            with open(cookies_file, 'r') as file:
                cookies = json.load(file)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
