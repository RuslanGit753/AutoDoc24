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

    with allure.step("Проверка вакансии в избранном, 1 вакансия"):
        fav_vac = page.add_fav_vacancies()
        assert len(fav_vac) == 1
