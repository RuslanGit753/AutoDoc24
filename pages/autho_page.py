from utils.config import Config
from pages.base_page import BasePage
from utils.locators import AuthPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class AuthorizationPage(BasePage):
    def open_login_form(self, email, password):
        self.open(Config.BASE_URL)
        self.find(AuthPageLocators.auth_button).click()
        self.find(AuthPageLocators.email_field).send_keys(email)
        self.find(AuthPageLocators.password_field).send_keys(password)
        self.find(AuthPageLocators.submit_button).click()

        self.find(AuthPageLocators.account).click()
        self.find(AuthPageLocators.account_link).click()

    def check_account_url(self):
        WebDriverWait(self.driver, 10).until(
        EC.url_contains("/applicant/account"))
        return self.driver.current_url.endswith("/applicant/account")
