import allure
import pytest
from pages_ui.applicant_page import UpdInfoApplPage
from utils.gener_data import ApplTestData


@pytest.mark.smoke
@allure.feature("Тестирование соискателя")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест обновление телефона соискателя")
@allure.description("Убедиться что номер присутствует, "
                    "затем заменить на новый")
def test_upd_phone(driver):
    with allure.step("Инициализация драйвера"):
        page = UpdInfoApplPage(driver)

    with allure.step("Загрузка кук авторизации пользователя"):
        page.load_cookies()

    with allure.step("Убедится что поле номера не пустое"):
        old_phone = page.get_old_phone()
        assert old_phone != ""

    with allure.step("Заменить старый номер на новый"):
        page.add_new_phone(ApplTestData.upd_tel_num)

    with allure.step("Записать длбавленный номер в переменную"):
        new_phone = page.save_new_phone()

    with allure.step("Проверить что номер добавился"):
        assert new_phone == ApplTestData.upd_tel_num
