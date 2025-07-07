import os
import requests
from faker import Faker
from body_api.user_id import user_id_1
from body_api.token_appl import autho_bearer_1


fake = Faker()


class CreateApplicantApi:
    """Класс создания соискателя"""
    def __init__(self, url):
        self.url = url

    def create_account_appl(self, first_name, last_name,
                            email_user1, password_user1):
        """Создание аккаунта соискателя"""
        url = f"{self.url}/registration/applicant/"
        data = {
                    "email": email_user1,
                    "password": password_user1,
                    "first_name": first_name,
                    "last_name": last_name
                }
        body = requests.post(url, data=data)
        return body

    def verific_account_appl(self, email_user1, code):
        """Отпрвка 4-х значного кода, который пришел на указанную почту"""
        url = f"{self.url}/registration/verify/"
        # Тело запроса
        data = {
                    "email": email_user1,
                    "otp": code
                }
        body = requests.post(url, data=data)
        return body


class LoginAppApplicantApi:
    """Класс авторизации соискателя"""
    def __init__(self, url):
        self.url = url

    def login_save_cookies_appl(self, email_user1, password_user1):
        """Авторизация пользователя с сохранение токена """
        url = f"{self.url}/login/"
        # Тело запроса
        data = {
            "email": email_user1,
            "password": password_user1
        }
        body = requests.post(url, data=data)

        # Убедимся, что директория существует
        if not os.path.exists('body_api'):
            os.makedirs('body_api')

        # Извлекаем значение access из тела ответа
        autho_bearer = body.json().get("access")

        # Сохраняем токен в файл token_appl
        with open(os.path.join('body_api', 'token_appl.py'), 'w') as file:
            file.write(f"autho_bearer_1 = '{autho_bearer}'")
        return body

    def login_appl(self, email_user1, password_user1):
        """Обычная авторизация пользователя, без сохранения токена"""
        url = f"{self.url}/login/"
        # Тело запроса
        data = {
            "email": email_user1,
            "password": password_user1
        }
        body = requests.post(url, data=data)
        return body

    def get_account_appl_api(self):
        """Получить персональные данные соискателя"""
        headers = {
            "Authorization": f"Bearer {autho_bearer_1}"
        }
        url = f"{self.url}/applicant/{user_id_1}"
        response = requests.get(url, headers=headers)
        return response


class DeleteApplicantApi:
    """Класс удаления соискателя"""
    def __init__(self, url):
        self.url = url

    def delete_account_appl_api(self, password_user2):
        """Удаление аккаунта соискателя"""
        headers = {
            "Authorization": f"Bearer {autho_bearer_1}"
        }
        # Тело запроса
        data = {
            "password": password_user2,
            "is_confirm": True
        }
        url = f"{self.url}/applicant/{user_id_1}/delete/"
        body = requests.delete(url, data=data, headers=headers)
        return body


class VacancyApi:
    """Класс работы с вакансиями для соискателя"""
    def __init__(self, url):
        self.url = url

    def get_vacancy_appl_api(self):
        """Поучить список вакансий"""
        headers = {
            "Authorization": f"Bearer {autho_bearer_1}"
        }
        url = f"{self.url}//vacancies/applicant/"
        body = requests.get(url, headers=headers)
        return body


class CreateResume:
    """Класс создания резюме"""
