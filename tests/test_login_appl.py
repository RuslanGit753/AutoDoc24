import os
import json
import pytest
from utils.config import Config
from pages.autho_page import AuthorizationPage


@pytest.mark.parametrize("username,password,cookie_file", [
    (Config.my_appl_name_1, Config.my_appl_pas_1, "user1.json"),
    (Config.my_appl_name_2, Config.my_appl_pas_2, "user2.json")
])
def test_login_successful(driver, username, password, cookie_file):
    page = AuthorizationPage(driver)
    page.open_login_form(username, password)
    assert page.check_account_url(), "URL не содержит '/applicant/account'"

    os.makedirs("cookies", exist_ok=True)
    with open(f"cookies/{cookie_file}", 'w') as file:
        json.dump(driver.get_cookies(), file, indent=2)
