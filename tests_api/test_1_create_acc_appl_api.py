import pytest
import allure
from utils.config import Config
from utils.gener_data import ApplTestData
from pages_api.appl_page_api import CreateApplicantApi


api = CreateApplicantApi(Config.BASE_URL_API)
first_name = Config.appl_first_name_1
last_name = Config.appl_last_name_1
email_user1 = Config.my_appl_mail_1
password_user1 = Config.my_appl_pas_1


@allure.feature("Тестирование API соискателя")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест создания профиля")
@allure.description("Обязательные поля: имя, фамилия, почта и пароль")
@pytest.mark.api
@pytest.mark.smoke
def test_create_account_appl():
    with allure.step("Создание аккаунта соискателя"):
        response = api.create_account_appl(first_name, last_name,
                                           email_user1, password_user1)
    with allure.step("Проверка статус кода для регистрации == 201"):
        assert response.status_code == 201


@allure.feature("Тестирование API соискателя")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Пдтверждение регистрации")
@allure.description(f"Код приходит на почту {email_user1}")
@pytest.mark.api
@pytest.mark.smoke
def test_verific_account_appl():
    with allure.step("Отправка 4-х значного кода"):
        # Ввести в течении 1 мин
        code = input("Введите 4-значный код из письма: ")
        response = api.verific_account_appl(email_user1, code)

    with allure.step("Проверка статус кода для верификации == 200"):
        assert response.status_code == 200


@allure.feature("Тестирование API соискателя")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Позитивные проверки поля имени")
@allure.description("Валидация поля без создания аккаунта")
@pytest.mark.api
@pytest.mark.positive_test
@pytest.mark.parametrize("first_name, last_name, email, password", [
    ("Антон", last_name, ApplTestData.gen_email(), "Enter1_753"),
    ("Anton", last_name, ApplTestData.gen_email(), "Enter1_753"),
    (" Антон", last_name, ApplTestData.gen_email(), "Enter1_753"),
    ("Антон ", last_name, ApplTestData.gen_email(), "Enter1_753"),
    ("Антон-Аврелий", last_name, ApplTestData.gen_email(), "Enter1_753"),
    ("Антон Аврелий", last_name, ApplTestData.gen_email(), "Enter1_753"),
    ("антон", last_name, ApplTestData.gen_email(), "Enter1_753"),
    ("а", last_name, ApplTestData.gen_email(), "Enter1_753"),
    ("а" * 30, last_name, ApplTestData.gen_email(), "Enter1_753")
])
def test_first_name_pos(first_name, last_name, email, password):
    with allure.step("Создание аккаунта соискателя"):
        response = api.create_account_appl(first_name, last_name,
                                           email, password)

    with allure.step("Проверка статус кода для регистрации == 201"):
        assert response.status_code == 201


@allure.feature("Тестирование API соискателя")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Негативные проверки поля имени")
@allure.description("Валидация поля без создания аккаунта")
@pytest.mark.api
@pytest.mark.negative_test
@pytest.mark.parametrize("first_name, last_name, email, password", [
    ("-Антон", last_name, ApplTestData.gen_email(), "Enter1_753"),
    ("Anton-", last_name, ApplTestData.gen_email(), "Enter1_753"),
    ("Антон23", last_name, ApplTestData.gen_email(), "Enter1_753"),
    ("", last_name, ApplTestData.gen_email(), "Enter1_753"),
    ("Антон%№", last_name, ApplTestData.gen_email(), "Enter1_753"),
    ("А" * 31, last_name, ApplTestData.gen_email(), "Enter1_753")
])
def test_first_name_neg(first_name, last_name, email, password):
    with allure.step("Создание аккаунта соискателя"):
        response = api.create_account_appl(first_name, last_name,
                                           email, password)

    with allure.step("Проверка статус кода для регистрации == 400"):
        assert response.status_code == 400


@allure.feature("Тестирование API соискателя")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Позитивные проверки поля фамилии")
@allure.description("Валидация поля без создания аккаунта")
@pytest.mark.api
@pytest.mark.positive_test
@pytest.mark.parametrize("first_name, last_name, email, password", [
    ("Антон", "Evans", ApplTestData.gen_email(), "Enter1_753"),
    ("Антон", "Петров", ApplTestData.gen_email(), "Enter1_753"),
    ("Антон", " Петров", ApplTestData.gen_email(), "Enter1_753"),
    ("Антон", "Петров  Прокофьев", ApplTestData.gen_email(), "Enter1_753"),
    ("Антон", "Петров-Прокофьев", ApplTestData.gen_email(), "Enter1_753"),
    ("Антон", "evans", ApplTestData.gen_email(), "Enter1_753"),
    ("Антон", "e", ApplTestData.gen_email(), "Enter1_753"),
    ("Антон", "e" * 30, ApplTestData.gen_email(), "Enter1_753")
])
def test_last_name_pos(first_name, last_name, email, password):
    with allure.step("Создание аккаунта соискателя"):
        response = api.create_account_appl(first_name, last_name,
                                           email, password)

    with allure.step("Проверка статус кода для регистрации == 201"):
        assert response.status_code == 201


@allure.feature("Тестирование API соискателя")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Негативные проверки поля фамилии")
@allure.description("Валидация поля без создания аккаунта")
@pytest.mark.api
@pytest.mark.negative_test
@pytest.mark.parametrize("first_name, last_name, email, password", [
    ("Антон", "-Evans", ApplTestData.gen_email(), "Enter1_753"),
    ("Антон", "Evans-", ApplTestData.gen_email(), "Enter1_753"),
    ("Антон", "Evans4543", ApplTestData.gen_email(), "Enter1_753"),
    ("Антон", "Evans;%;", ApplTestData.gen_email(), "Enter1_753"),
    ("Антон", "", ApplTestData.gen_email(), "Enter1_753"),
    ("Антон", "E" * 31, ApplTestData.gen_email(), "Enter1_753")
])
def test_last_name_neg(first_name, last_name, email, password):
    with allure.step("Создание аккаунта соискателя"):
        response = api.create_account_appl(first_name, last_name,
                                           email, password)

    with allure.step("Проверка статус кода для регистрации == 400"):
        assert response.status_code == 400


@allure.feature("Тестирование API соискателя")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Позитивные проверки поля почты")
@allure.description("Валидация поля без создания аккаунта")
@pytest.mark.api
@pytest.mark.positive_test
@pytest.mark.parametrize("first_name, last_name, email, password", [
    ("Антон", "Петров", "." + ApplTestData.gen_email(), "Enter1_753"),
    ("Антон", "Петров", ".." + ApplTestData.gen_email(), "Enter1_753"),
    ("Антон", "Петров", ApplTestData.gen_email() + ".", "Enter1_753"),
    ("Антон", "Петров", ApplTestData.gen_email() + "..", "Enter1_753"),
    ("Антон", "Петров", "-" + ApplTestData.gen_email(), "Enter1_753"),
    ("Антон", "Петров", "--" + ApplTestData.gen_email(), "Enter1_753"),
    ("Антон", "Петров", ApplTestData.gen_email() + "-", "Enter1_753"),
    ("Антон", "Петров", ApplTestData.gen_email() + "--", "Enter1_753"),
    ("Антон", "Петров", ApplTestData.gen_letter() + "@b.cd", "Enter1_753"),
    ("Антон", "Петров", ApplTestData.gen_letter() * 243 + "@domein.com",
     "Enter1_753")
])
def test_mail_pos(first_name, last_name, email, password):
    with allure.step("Создание аккаунта соискателя"):
        response = api.create_account_appl(first_name, last_name,
                                           email, password)

    with allure.step("Проверка статус кода для регистрации == 201"):
        assert response.status_code == 201


@allure.feature("Тестирование API соискателя")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Негативные проверки поля почты")
@allure.description("Валидация поля без создания аккаунта")
@pytest.mark.api
@pytest.mark.negative_test
@pytest.mark.parametrize("first_name, last_name, email, password", [
    ("Антон", "Петров", "." + ApplTestData.gen_email(), "Enter1_753"),
    ("Антон", "Петров", ".." + ApplTestData.gen_email(), "Enter1_753"),
    ("Антон", "Петров", ApplTestData.gen_email() + ".", "Enter1_753"),
    ("Антон", "Петров", ApplTestData.gen_email() + "..", "Enter1_753"),
    ("Антон", "Петров", "-" + ApplTestData.gen_email(), "Enter1_753"),
    ("Антон", "Петров", "--" + ApplTestData.gen_email(), "Enter1_753"),
    ("Антон", "Петров", ApplTestData.gen_email() + "-", "Enter1_753"),
    ("Антон", "Петров", ApplTestData.gen_email() + "--", "Enter1_753"),
    ("Антон", "Петров", ApplTestData.gen_letter() + "@b.c", "Enter1_753"),
    ("Антон", "Петров", ApplTestData.gen_letter() * 244 + "@domein.com",
     "Enter1_753")
])
def test_mail_neg(first_name, last_name, email, password):
    with allure.step("Создание аккаунта соискателя"):
        response = api.create_account_appl(first_name, last_name,
                                           email, password)

    with allure.step("Проверка статус кода для регистрации == 400"):
        assert response.status_code == 400


@allure.feature("Тестирование API соискателя")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Позитивные проверки поля пароль")
@allure.description("Валидация поля без создания аккаунта")
@pytest.mark.api
@pytest.mark.positive_test
@pytest.mark.parametrize("first_name, last_name, email, password", [
    ("Антон", "Петров", ApplTestData.gen_email(),
     ApplTestData.gen_pas(length=8)),
    ("Антон", "Петров", ApplTestData.gen_email(),
     ApplTestData.gen_pas(length=50)),
    ("Антон", "Петров", ApplTestData.gen_email(),
     ApplTestData.gen_registr(upper_case=False)),
    ("Антон", "Петров", ApplTestData.gen_email(),
     ApplTestData.gen_non_num()),
    ("Антон", "Петров", ApplTestData.gen_email(),
     ApplTestData.gen_non_spec_chars())
])
def test_password_pos(first_name, last_name, email, password):
    with allure.step("Создание аккаунта соискателя"):
        response = api.create_account_appl(first_name, last_name,
                                           email, password)

    with allure.step("Проверка статус кода для регистрации == 201"):
        assert response.status_code == 201


@allure.feature("Тестирование API соискателя")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Негативные проверки поля пароль")
@allure.description("Валидация поля без создания аккаунта")
@pytest.mark.api
@pytest.mark.negative_test
@pytest.mark.parametrize("first_name, last_name, email, password", [
    ("Антон", "Петров", ApplTestData.gen_email(),
     ApplTestData.gen_pas(length=7)),
    ("Антон", "Петров", ApplTestData.gen_email(),
     ApplTestData.gen_pas(length=51)),
    ("Антон", "Петров", ApplTestData.gen_email(),
     " " + ApplTestData.gen_registr()),
    ("Антон", "Петров", ApplTestData.gen_email(),
     ApplTestData.gen_num(digits=10)),
    ("Антон", "Петров", ApplTestData.gen_email(), "ОЛРрорупр"),
    ("Антон", "Петров", ApplTestData.gen_email(), "%;::?%?;№()")
])
def test_password_neg(first_name, last_name, email, password):
    with allure.step("Создание аккаунта соискателя"):
        response = api.create_account_appl(first_name, last_name,
                                           email, password)

    with allure.step("Проверка статус кода для регистрации == 400"):
        assert response.status_code == 400
