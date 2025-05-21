from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



def get_chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1440,1024')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=chrome_options, service=service)
    return driver
