from pages.account_page import AccountPage
from utils.config import Config


def test_main_page(driver):
    page = AccountPage(driver)
    email = page.account_email()
    print(email)
    assert '/applicant/account' in driver.current_url
    assert email == Config.my_appl_name_1
