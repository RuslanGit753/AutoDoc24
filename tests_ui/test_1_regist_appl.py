import pytest
import allure
from utils.config import Config
from pages_ui.applicant_page import RegistrApplPage


@pytest.mark.smoke
@allure.feature("Тестирование соискателя")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест на удаление аккаунта соискателя")
def test_regist_appl(driver):
    with allure.step("Инициализация класса удаления аккаунта"):
        page = RegistrApplPage(driver)

    with allure.step("Открытие формы регистрации соискателя"):
        page.open_form_regist_appl()

    with allure.step("Шаг первый: заполнение данных для регистрации"):
        page.send_data_appl(Config.appl_first_name_1, Config.appl_last_name_1,
                            Config.my_appl_mail_1, Config.my_appl_pas_1)

    with allure.step("Шаг второй: ввести 4-x значный код подтверждения"):
        text_result = page.send_code()

    with allure.step("Проверка сообщения: Регистрация завершена"):
        assert text_result is True
