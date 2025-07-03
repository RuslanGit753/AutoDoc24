import os
import json
import pytest
import allure
from utils.config import Config
from pages_ui.autho_page import AuthorizationPage


@pytest.mark.smoke
@pytest.mark.parametrize("username, password, cookie_file", [
    (Config.my_appl_name_1, Config.my_appl_pas_1, "user1.json")
])
@allure.feature("Тестирование соискателя")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Тест авторизации пользователя")
@allure.description("Добавить первую вакансию в избранное")
def test_login_successful(driver, username, password, cookie_file):
    with allure.step("Инициализация драйвера"):
        page = AuthorizationPage(driver)

    with allure.step("Ввод логина и пароля"):
        page.open_login_form(username, password)
        assert page.check_account_url_appl(), "URL содержит '/applicant/account'"

    with allure.step("Добавление скриншота"):
        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot, name='Личный кабинет',
                      attachment_type=allure.attachment_type.PNG)

    with allure.step("Сохранения кук авторизации"):
        os.makedirs("cookies", exist_ok=True)
        with open(f"cookies/{cookie_file}", 'w') as file:
            json.dump(driver.get_cookies(), file, indent=2)
