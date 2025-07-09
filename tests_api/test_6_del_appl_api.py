import pytest
import allure
from utils.config import ConfigAppl
from utils.user_id_appl_api import user_id_appl
from utils.token_appl_1_api import bearer_appl_1
from pages_api.appl_page_api import DeleteApplicantApi


api = DeleteApplicantApi(ConfigAppl.BASE_URL_API)
password_user1 = ConfigAppl.my_appl_pas_1


@allure.feature("Тестирование API соискателя")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест на удаление")
@allure.description("Удаление профиля")
@pytest.mark.api
@pytest.mark.smoke
def test_delete_account_appl_api():
    with allure.step("Отправка DELETE-запроса к"
                     f"/applicant/{user_id_appl}/delete/"):
        response = api.delete_account_appl_api(password_user1, 
                                               bearer_appl_1,
                                               user_id_appl)

    with allure.step("Проверка статус кода == 204"):
        assert response.status_code == 204
