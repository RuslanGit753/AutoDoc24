import os
import time
import pytest
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()
username_value = os.getenv('my_appli_name_1')
password_value = os.getenv('my_appli_pas_1')

@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1440,1024') 
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=chrome_options, service=service)
    driver.get('https://rabota.ktsf.ru/vacancies')
    yield driver


@pytest.fixture()
def wait(driver):
    return WebDriverWait(driver, 5, poll_frequency=1)
