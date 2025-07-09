import pytest
import allure
from utils.config import ConfigAppl
from utils.user_id_appl_api import user_id_appl
from utils.token_appl_1_api import bearer_appl_1
from pages_api.appl_page_api import LoginAppApplicantApi


api = LoginAppApplicantApi(ConfigAppl.BASE_URL_API)


@allure.feature("Тестирование API соискателя")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест получение страницы пользователя")
@allure.description("Получить персональные данные "
                    "соискателя и убедится, что почта "
                    "соответствует пользователю")
@pytest.mark.api
@pytest.mark.smoke
def test_get_account_appl_api():
    with allure.step(f"Отправка GET-запроса к /applicant/{user_id_appl}"):
        response = api.get_account_appl_api(bearer_appl_1, user_id_appl)

    with allure.step("Проверить почту пользователя"):
        mail = response.json()
        assert mail["user"]["email"] == ConfigAppl.my_appl_mail_1

    with allure.step("Проверка статус кода == 200"):
        assert response.status_code == 200
