import os
import json
from utils.config import Config
from pages.base_page import BasePage
from utils.locators import PersonalAccount


class AccountPage(BasePage):
    def account_email(self):
        self.open(Config.BASE_URL)
        self.clear_cookies()
        self.load_user_cookies(1)
        self.open(Config.account_url)
        email_acc = self.find(PersonalAccount.email_account).get_attribute('value')
        return email_acc
