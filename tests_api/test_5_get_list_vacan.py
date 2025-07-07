import pytest
import allure
from utils.config import Config
from pages_api.appl_page_api import VacancyApi


api = VacancyApi(Config.BASE_URL_API)


@allure.feature("Тестирование API соискателя")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Тест на получение списка вакансий")
@allure.description(
    "Соискатель получает полный список вакансий")
@pytest.mark.api
@pytest.mark.positive_test
def test_get_vacancy_list():
    with allure.step("Отправить GET-запрос на получение списка вакансий"):
        response = api.get_vacancy_appl_api()

    with allure.step("Проверка статус кода == 200"):
        assert response.status_code == 200
