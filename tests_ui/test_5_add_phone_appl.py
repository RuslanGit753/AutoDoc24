import allure
import pytest
from pages_ui.applicant_page import AddInfoApplPage
from utils.gener_data import ApplTestData


@pytest.mark.smoke
@allure.feature("Тестирование соискателя")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест добавления телефона соискателя")
@allure.description("Добавить номер телефона и проверить, "
                    "что он отображается после сохранения")
def test_add_phone(driver):
    with allure.step("Инициализация драйвера"):
        page = AddInfoApplPage(driver)

    with allure.step("Загрузка кук авторизации пользователя"):
        page.load_cookies()

    with allure.step("Добавление номера телефона в личном кабинете"):
        page.add_phone(ApplTestData.tel_num)

    with allure.step("Сохранение добавленного номера"):
        save_phone = page.save_add_phone()

    with allure.step("Проверка сохраненного номера после добавления"):
        assert save_phone == ApplTestData.tel_num
