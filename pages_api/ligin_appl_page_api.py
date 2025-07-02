import os
import json
import allure
import requests


class Login:
    def __init__(self, url):
        self.url = url

    @allure.step('Авторизация соискателя и сохранение токена')
    def login_save_cookies_appl(self, email_user1, password_user1):
        url = f"{self.url}/login/"
        data = {
            "email": email_user1,
            "password": password_user1
        }
        body = requests.post(url, data=data)

        # Убедимся, что директория существует
        if not os.path.exists('body_api'):
            os.makedirs('body_api')

        # Сохраняем токен в файл в формате JSON
        with open(os.path.join('body_api', 'token_appl.json'), 'w') as file:
            json.dump(body.json(), file, indent=4)
        return body

    @allure.step('Авторизация соискателя')
    def login_appl(self, email_user1, password_user1):
        url = f"{self.url}/login/"
        data = {
            "email": email_user1,
            "password": password_user1
        }
        body = requests.post(url, data=data)
        return body
