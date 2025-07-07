import pytest
import allure
from utils.config import Config
from body_api.user_id import user_id_1
from pages_api.appl_page_api import LoginAppApplicantApi


api = LoginAppApplicantApi(Config.BASE_URL_API)


@allure.feature("Тестирование API соискателя")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест получение страницы пользователя")
@allure.description("Получить персональные данные соискателя")
@pytest.mark.api
@pytest.mark.smoke
def test_get_account_appl_api():
    with allure.step(f"Отправка GET-запроса к /applicant/{user_id_1}"):
        response = api.get_account_appl_api()

    with allure.step("Проверка статус кода == 200"):
        assert response.status_code == 200
