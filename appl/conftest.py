import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from dotenv import load_dotenv

load_dotenv()
username_value = os.getenv('my_appli_name_1')
password_value = os.getenv('my_appli_pas_1')


@pytest.fixture()
def chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1440,1024') 
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=chrome_options, service=service)
    driver.get('https://job-frontend-alpha.vercel.app/vacancies')
    yield driver
    driver.quit()

@pytest.fixture()
def firefox():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--window-size=1440,1024')
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(options=firefox_options, service=service)
    driver.get('https://job-frontend-alpha.vercel.app/vacancies')
    yield driver
    driver.quit()


@pytest.fixture()
def chrome_wait(chrome):
    return WebDriverWait(chrome, 5, poll_frequency=1)

@pytest.fixture()
def firefox_wait(firefox):
    return WebDriverWait(firefox, 5, poll_frequency=1)
