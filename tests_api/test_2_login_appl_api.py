import pytest
import allure
from utils.config import Config
from pages_api.appl_page_api import LoginAppApplicantApi


api = LoginAppApplicantApi(Config.BASE_URL_API)
email_user1 = Config.my_appl_name_1
password_user1 = Config.my_appl_pas_1


@allure.feature("Тестирование API соискателя")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Тест на авторизацию")
@allure.description(
    "Проверка успешной авторизации и сохранения токена")
@pytest.mark.api
@pytest.mark.smoke
def test_login_save_cookies_appl():
    with allure.step("Отправка POST-запроса к /login/"):
        response = api.login_save_cookies_appl(
            email_user1, password_user1)

    with allure.step("Проверка статус кода == 200"):
        assert response.status_code == 200
    allure.attach(response.text,
                  'Response Body', allure.attachment_type.TEXT)


@allure.feature("Тестирование API соискателя")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Авторизация: невалидный email")
@allure.description("Проверка системы на неверные данные почты")
@pytest.mark.api
@pytest.mark.negative_test
@pytest.mark.parametrize("email, password", [
    ("", password_user1),
    (".lol126lols@gmail.com", password_user1),
    ("lol126lols@gmail.com.", password_user1),
    ("lol126..lols@gmail.com", password_user1),
    ("lol126l__ols@gmail.com", password_user1),
    ("lol126l--ols@gmail.com", password_user1),
    ("-lol126lols@gmail.com", password_user1),
    ("lol126lols@gmail.com-", password_user1),
    ("l" * 51, password_user1)
])
@allure.title("Невалидный email: {email}")
def test_mail_appl_neg(email, password):
    with allure.step("Отправка POST-запроса к /login/"):
        response = api.login_appl(email, password)

    with allure.step("Проверка статус кода == 400 или 401"):
        assert response.status_code == 400 or 401
    allure.attach(response.text,
                  'Response Body', allure.attachment_type.TEXT)


@allure.feature("Тестирование API соискателя")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Авторизация: невалидный пароль")
@allure.description("Проверка системы на неверные данные пароля")
@pytest.mark.api
@pytest.mark.negative_test
@pytest.mark.parametrize("email, password", [
    (email_user1, ""),
    (email_user1, "g" * 51),
    (email_user1, "Enter14"),
    (email_user1, "Ente r142"),
    (email_user1, "РОырвфлр"),
    (email_user1, "FGDCHGGJG"),
    ("", ""),
    ("0", "0")
])
def test_password_appl_neg(email, password):
    with allure.step("Отправка POST-запроса к /login/"):
        response = api.login_appl(email, password)

    with allure.step("Проверка статус кода == 400 или 401"):
        assert response.status_code == 400 or 401
        allure.attach(response.text,
                      'Response Body', allure.attachment_type.TEXT)
