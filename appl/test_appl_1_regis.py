import os
import time
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--window-size=1440,1024') 

load_dotenv()
username_value = os.getenv('my_appli_name_1')
password_value = os.getenv('my_appli_pas_1')

driver = webdriver.Chrome(options=chrome_options)

login_URL = "https://rabota.ktsf.ru/vacancies"
driver.get(login_URL)

enter = driver.find_element("class name", "Header_header__authorized__l3dJL")
driver.execute_script("arguments[0].click();", enter)
registration = driver.find_element('xpath', '//button[@class="ModalLogIn_link__aooLt ModalLogIn_underline__d46Fj"]')
driver.execute_script("arguments[0].click();", registration)
applicant = driver.find_element('xpath', '//label[text()="Я ищу работу"]').click()
next = driver.find_element('xpath', '//button[text()="Продолжить"]').click()

first_name = driver.find_element('xpath', '//input[@id="first_name"]')
first_name.send_keys('Агнешка')

last_name = driver.find_element('xpath', '//input[@id="last_name"]')
last_name.send_keys('Бжезинская')

email = driver.find_element('xpath', '//input[@id="email"]')
email.send_keys(username_value)

password = driver.find_element('xpath', '//input[@type="password"]')
password.send_keys(password_value)

registration2 = driver.find_element('xpath', '//button[text()="Зарегистрироваться"]').click()