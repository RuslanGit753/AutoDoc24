import pytest
from utils.config import Config
from pages.autho_page import AuthorizationPage


@pytest.mark.parametrize("username,password", [
    (Config.my_appl_name_1, Config.my_appl_pas_1),
    (Config.my_appl_name_2, Config.my_appl_pas_2)
])
def test_login_successful(driver, username, password):
    page = AuthorizationPage(driver)
    page.open_login_form(username, password)

    assert page.check_account_url(), "URL не содержит '/applicant/account'"
