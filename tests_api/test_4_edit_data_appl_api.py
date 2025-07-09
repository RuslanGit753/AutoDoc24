import pytest
import allure
from utils.config import ConfigAppl
from pages_api.appl_page_api import EditingApplAccAppi
from utils.user_id_appl_api import user_id_appl
from utils.token_appl_1_api import bearer_appl_1
from utils.gener_data import ApplTestData


api = EditingApplAccAppi(ConfigAppl.BASE_URL_API)
email = ConfigAppl.my_appl_mail_1
phone_appl = ApplTestData.tel_num
first_name = ConfigAppl.appl_first_name_1
last_name = ConfigAppl.appl_last_name_1


@allure.feature("Тестирование API соискателя")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Добавить номер телефона")
@allure.description("Добавить номер и проверить что номер отображается")
@pytest.mark.api
@pytest.mark.positive_test
@pytest.mark.parametrize("email, phone, first_name, last_name", [
    (email, phone_appl, first_name, last_name),
    (email, "+7(356)8964532", first_name, last_name),
    (email, "+7(356)896-45-32", first_name, last_name)
])
def test_add_phone_pos(email, phone, first_name, last_name):
    with allure.step("Отправка PATCH-запроса к /applicant/user_id/"):
        response = api.add_phone_appl_api(email, phone, 
                                          first_name, last_name, 
                                          bearer_appl_1, user_id_appl)

    with allure.step("Проверка статус кода == 200"):
        assert response.status_code == 200

    with allure.step("Проверить номер в теле ответа"):
        mail = response.json()
        assert mail["user"]["phone"] == phone_appl


@allure.feature("Тестирование API соискателя")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Добавить номер телефона")
@allure.description("Добавить номер и проверить что номер отображается")
@pytest.mark.api
@pytest.mark.negative_test
@pytest.mark.parametrize("email, phone, first_name, last_name", [
    (email, "", first_name, last_name),
    (email, "7(356)8964532", first_name, last_name),
    (email, "+(356)896-45-32", first_name, last_name),
    (email, "+7(356)896-45-329", first_name, last_name),
    (email, "-7(356)896-45-32", first_name, last_name),
    (email, "+7(000)000-00-00", first_name, last_name),
    (email, "+7 356 896-45-32", first_name, last_name),
    (email, "+9(356)896-45-32", first_name, last_name)
])
def test_add_phone_neg(email, phone, first_name, last_name):
    with allure.step("Отправка PATCH-запроса к /applicant/user_id/"):
        response = api.add_phone_appl_api(email, phone, 
                                          first_name, last_name, 
                                          bearer_appl_1, user_id_appl)

    with allure.step("Проверка статус кода == 400"):
        assert response.status_code == 400
