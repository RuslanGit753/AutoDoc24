import os
import json
import pytest
import allure
from utils.config import ConfigAppl
from pages_ui.applicant_page import AuthorizationPage


@pytest.mark.smoke
@pytest.mark.parametrize("username, password, cookie_file", [
    (ConfigAppl.my_appl_mail_1, ConfigAppl.my_appl_pas_1, "user1.json")
])
@allure.feature("Тестирование соискателя")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Тест авторизации пользователя")
@allure.description("Авторизоваться и проверить"
                    "почту соискателя в личном кабинете")
def test_login_successful(driver, username, password, cookie_file):
    with allure.step("Инициализация класса авторизации соискателя"):
        page = AuthorizationPage(driver)

    with allure.step("Ввод логина и пароля"):
        page.open_login_form(username, password)

    with allure.step("Открытие личного кабинета"
                     "и извлечение почты соискателя"):
        account = page.open_acc_appl()

    with allure.step("Проверка почты пользователя"):
        assert account == ConfigAppl.my_appl_mail_1

    with allure.step("Сохранения кук авторизации"):
        os.makedirs("cookies", exist_ok=True)
        with open(f"cookies/{cookie_file}", 'w') as file:
            json.dump(driver.get_cookies(), file, indent=2)
