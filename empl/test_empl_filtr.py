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
username_value = os.getenv('empl_name_1')
password_value = os.getenv('empl_pas_1')

driver = webdriver.Chrome(options=chrome_options)

login_URL = "https://job-frontend-weld.vercel.app/"
driver.get(login_URL)

authorized = driver.find_element("class name", "Header_header__authorized__l3dJL")
driver.execute_script("arguments[0].click();", authorized)

username = driver.find_element('xpath', '//input[@name="email" and @type="email"]')
username.clear()
username.send_keys(username_value)

password = driver.find_element('xpath', '//input[@type="password"]')
password.clear()
password.send_keys(password_value)

button = driver.find_element('class name', 'ModalLogIn_btn__evz5S').click()
time.sleep(4)
driver.refresh()
time.sleep(3)

search = driver.find_element('class name', 'Filter_filter__search__N__0c')
driver.execute_script("arguments[0].click();", search)
time.sleep(3)

# Поиск по зарплате
salary = driver.find_element('xpath', '//div[@class="Sorter_filterItem__Yt8oU"][1]').click()
input_salary = driver.find_element('xpath', '//label[@class="Sorter_inputContainer__Sz27t"]')
input_salary.send_keys('100000')
salary = driver.find_element('xpath', '//button[@class="Sorter_applyButtonSal__P_Bvi"]').click()
time.sleep(3)

# Поиск по графику
chart = driver.find_element('xpath', '//div[@class="Sorter_filterItem__Yt8oU"][2]').click()
full_day = driver.find_element('xpath', '//label[@class="Sorter_checkboxLabel__UsLwi"][1]').click()
time.sleep(3)

# Поиск по формату
format_sorter = driver.find_element('xpath', '//div[@class="Sorter_filterItem__Yt8oU"][3]').click()
full_employ = driver.find_element('xpath', '//label[@class="Sorter_checkboxLabel__UsLwi"][1]').click()
time.sleep(3)

# Поиск по образованию
education = driver.find_element('xpath', '//div[@class="Sorter_filterItem__Yt8oU"][4]').click()
time.sleep(1)

# среднее 1, среднее специальное 2, высшее 3, не требуется 4
level_educ = driver.find_element('xpath', '//div/label[3]').click()
time.sleep(3)

# Подчет количества вакансий
num_vacan = driver.find_elements('class name', 'ApplicantCard_card__hVM1T')
sum_vacan = int(len(num_vacan))
print(f'Количество вакансий: {sum_vacan}')
time.sleep(3)

# Извлекаем данные карточек
card_vacan = [h.text.split('\n') for h in num_vacan]
table_columns = ['Имя', 'Возраст', 'Профессия', 'Город', 'Опыт', 'Зарплата']

df = pd.DataFrame(data=card_vacan, columns=table_columns)
print(df)
# df.to_csv('empl_autho.csv', index=None)