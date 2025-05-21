from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService



def get_driver(browser_name):
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1440,1024')
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(options=options, service=service)
        return driver
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(options=options, service=service)
        driver.maximize_window()
        return driver
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
