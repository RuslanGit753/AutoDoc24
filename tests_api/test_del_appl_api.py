import pytest
import allure
from utils.config import Config
from body_api.user_id import user_id_1
from pages_api.appl_page_api import PageApplicantApi


api = PageApplicantApi(Config.BASE_URL_API)
password_user1 = Config.my_appl_pas_1


@allure.feature("Тестирование API")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест на удаление соискателя")
@allure.description("Удаление соискателя")
@pytest.mark.api
@pytest.mark.smoke
def test_delete_account_appl_api():
    with allure.step(f"Отправка DELETE-запроса к /applicant/{user_id_1}/delete"):
        response = api.delete_account_appl_api(password_user1)
    with allure.step("Проверка статус кода == 204"):
        assert response.status_code == 204
