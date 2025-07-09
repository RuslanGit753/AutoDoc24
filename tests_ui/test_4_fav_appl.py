import allure
import pytest
from pages_ui.applicant_page import FavoritesPage


@pytest.mark.smoke
@allure.feature("Тестирование соискателя")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Тест добавления вакансии в избранное")
@allure.description("Добавить первую вакансию в избранное")
def test_add_fav_vacancies(driver):
    with allure.step("Инициализация драйвера"):
        page = FavoritesPage(driver)

    with allure.step("Загрузка кук авторизации пользователя"):
        page.load_cookies()

    with allure.step("Добавление первой вакансии из списка в избранное"):
        page.add_fav_vacancies()

    with allure.step("Проверка вакансии в избранном, 1 вакансия"):
        fav_vac = page. check_vacan_fav()
        assert len(fav_vac) == 1
