import os
import requests
from faker import Faker


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

        # Извлекаем значение access из тела ответа
        autho_bearer = body.json().get("access")

        # Сохраняем токен в файл token_appl
        with open(os.path.join('utils', 'token_appl_1_api.py'), 'w') as file:
            file.write(f"bearer_appl_1 = '{autho_bearer}'")
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

    def get_account_appl_api(self, bearer_appl_1, user_id_appl):
        """Получить персональные данные соискателя"""
        headers = {
            "Authorization": f"Bearer {bearer_appl_1}"
        }
        url = f"{self.url}/applicant/{user_id_appl}"
        response = requests.get(url, headers=headers)
        return response


class DeleteApplicantApi:
    """Класс удаления соискателя"""
    def __init__(self, url):
        self.url = url

    def delete_account_appl_api(self, password_user1, 
                                bearer_appl_1, user_id_appl):
        """Удаление аккаунта соискателя"""
        headers = {
            "Authorization": f"Bearer {bearer_appl_1}"
        }
        # Тело запроса
        data = {
            "password": password_user1,
            "is_confirm": True
        }
        url = f"{self.url}/applicant/{user_id_appl}/delete/"
        body = requests.delete(url, data=data, headers=headers)
        return body


class VacancyApi:
    """Класс работы с вакансиями для соискателя"""
    def __init__(self, url):
        self.url = url

    def get_vacancy_appl_api(self, bearer_appl_1):
        """Поучить список вакансий"""
        headers = {
            "Authorization": f"Bearer {bearer_appl_1}"
        }
        url = f"{self.url}//vacancies/applicant/"
        body = requests.get(url, headers=headers)
        return body


class EditingApplAccAppi:
    """Класс редактирования личного кабинета. 
    Можно отредактировать: имя, фамилию, номер телефона"""
    def __init__(self, url):
        self.url = url

    def add_phone_appl_api(self, email, phone, first_name, last_name, 
                           bearer_appl_1, user_id_appl):
        """Добавить или изменить номер телефона"""
        headers = {
                "Authorization": f"Bearer {bearer_appl_1}"
            }
        # Тело запроса
        data = {
            "email": email,
            "phone": phone,
            "first_name": first_name,
            "last_name": last_name
        }
        url = f"{self.url}/applicant/{user_id_appl}/"
        body = requests.patch(url, data=data, headers=headers)
        return body
