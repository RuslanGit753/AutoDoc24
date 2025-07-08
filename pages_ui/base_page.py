import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Класс для работы с веб-страницей"""
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        """Метод для открытия веб страницы"""
        self.driver.get(url)

    def find(self, locator, timeout=10):
        """Ожидание локатора элемента"""
        from selenium.common.exceptions import TimeoutException
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator))
        except TimeoutException:
            print(f"Элемент с локатором {locator} не найден"
                  f"в течение {timeout} секунд")

    def find_text(self, locator, text, timeout=10):
        """Ожидание локатора элемента с текстом"""
        from selenium.common.exceptions import TimeoutException
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            print(f"Текст из локатора {locator} не найден"
                  f"в течение {timeout} секунд")

    def find_elem_click(self, locator, timeout=10):
        """Ожидание пока элемент не станет кликабельным"""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))

    def find_elements(self, locator, timeout=10):
        """Ожидание появления нескольких элементов"""
        from selenium.common.exceptions import TimeoutException
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            print(f"Элементы с локатором {locator} не найдены"
                  f"в течение {timeout} секунд")

    def wait_for_url(self, pattern: str, timeout=10) -> None:
        """Ожидание появления необходимого URL"""
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(pattern))

    def scrol_page(self, element):
        """Прокрутка страницы до необходимого элемента"""
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center',"
            "behavior: 'smooth'});", element)

    def clear_cookies(self):
        """Очистка кук"""
        self.driver.delete_all_cookies()

    def load_user_cookies(self, user_number):
        """Загрузка кук на страницу"""
        cookies_file = os.path.join('cookies', f'user{user_number}.json')
        if os.path.exists(cookies_file):
            with open(cookies_file, 'r') as file:
                cookies = json.load(file)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
