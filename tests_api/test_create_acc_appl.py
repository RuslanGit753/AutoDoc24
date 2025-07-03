import pytest
import allure
from utils.config import Config
from pages_api.appl_page_api import PageApplicantApi


api = PageApplicantApi(Config.BASE_URL_API)
email_user1 = Config.my_appl_name_1
password_user1 = Config.my_appl_pas_1


@allure.feature("Тестирование API")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест создания профиля соискателя")
@allure.description(f"Создание профиля и верификация аккаунта 4-х значным кодом, котороый отправляется на указанную почту {email_user1}")
@pytest.mark.api
@pytest.mark.smoke
def test_create_account_appl():
    with allure.step(f"Создание аккаунта соискателя"):
        response = api.create_account_appl(email_user1, password_user1)

    with allure.step("Проверка статус кода для регистрации == 201"):
        assert response.status_code == 201


@allure.step("Подтверждения регистрации")
def test_verific_account_appl():
    with allure.step("Отправка 4-х значного кода"):
        response = api.verific_account_appl(email_user1)

    with allure.step("Проверка статус кода для верификации == 200"):
        assert response.status_code == 200
