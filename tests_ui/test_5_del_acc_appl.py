import pytest
import allure
from utils.config import Config
from pages_ui.applicant_page import DeleteApplPage


email = Config.my_appl_mail_1
password = Config.my_appl_pas_1


@pytest.mark.smoke
@allure.feature("Тестирование соискателя")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест на удаление аккаунта соискателя")
def test_delete_acc_appl(driver):
    with allure.step("Инициализация класса удаления аккаунта"):
        page = DeleteApplPage(driver)

    with allure.step("Загрузка кук авторизации пользователя"):
        page.load_cook_user()

    with allure.step("Удаление аккаунта"):
        result = page.dell_acc_appl()

    with allure.step("Проверка появления сообщения:"
                     "'Ваш аккаунт удалён'"):
        assert result is True
