import allure
import pytest
from pages_ui.applicant_page import ResVacPage


@pytest.mark.smoke
@allure.feature("Тестирование соискателя")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Тест отклика на вакансию")
@allure.description("Откликнуться на первую"
                    "вакансию из списка и проверить, что она"
                    "отображается в часте с работодателем. "
                    "Отклик на вакансию без резюме")
def test_resp_vac(driver):
    with allure.step("Инициализация драйвера"):
        page = ResVacPage(driver)

    with allure.step("Загрузка кук авторизации пользователя"):
        page.load_cookies()

    with allure.step("Отклик на первую вакансию из списка"):
        title_posit = page.respond_vac()

    with allure.step("Открытие чат с работодателем"):
        title_posit_chat = page.open_chat()

    with allure.step("Проверка отображения вакансии"
                     "в чате с работодателем,"
                     "по названию вакансии"):
        assert title_posit == title_posit_chat
