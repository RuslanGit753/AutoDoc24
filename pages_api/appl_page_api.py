import os
import requests
from body_api.user_id import user_id_1
from body_api.token_appl import autho_bearer_1


class PageApplicantApi:
    def __init__(self, url):
        self.url = url

    def create_account_appl(self, email_user1, password_user1):
        """Создание аккаунта соискателя"""
        url = f"{self.url}/registration/applicant/"
        data = {
                    "email": email_user1,
                    "password": password_user1,
                    "first_name": "ПРСрсриыс",
                    "last_name": "Зоиоирувв"
                }
        body = requests.post(url, data=data)
        return body


    def verific_account_appl(self, email_user1):
        """Отпрвка 4-х значного кода, который пришел на указанную почту"""
        url = f"{self.url}/registration/verify/"
        data = {
                    "email": email_user1,
                    "otp": 1238
                }
        body = requests.post(url, data=data)
        return body
    

    def login_save_cookies_appl(self, email_user1, password_user1):
        """Авторизация пользователя с сохранение токена """
        url = f"{self.url}/login/"
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


    def delete_account_appl_api(self, password_user2):
        """Удаление аккаунта соискателя"""
        headers = {
            "Authorization": f"Bearer {autho_bearer_1}"
        }
        data = {
            "password": password_user2,
            "is_confirm": True
        }
        url = f"{self.url}/applicant/{user_id_1}/delete/"
        body = requests.delete(url, data=data, headers=headers)
        return body
