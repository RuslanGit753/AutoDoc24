from utils.config import Config
from pages_ui.applicant_page import AccountPage


def test_valid_email(driver):
    page = AccountPage(driver)
    email = page.account_email()
    assert email == Config.my_appl_mail_1
