import pickle
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from conftest import username_value, password_value


def test_open_browser(chrome_wait, chrome):
     chrome_wait.until(EC.visibility_of_element_located((By.XPATH,
          '//button[@class="Header_header__authorized__l3dJL"]'))).click()
        
     chrome_wait.until(EC.visibility_of_element_located((By.XPATH,
          '//input[@type="email"]'))).send_keys(username_value)

     chrome_wait.until(EC.visibility_of_element_located((By.XPATH,
          '//input[@type="password"]'))).send_keys(password_value)

     chrome_wait.until(EC.visibility_of_element_located((By.XPATH,
          '//button[@type="submit"]'))).click()

     chrome_wait.until(EC.visibility_of_element_located((By.XPATH,
          '//div/div/button[@class="Icons_btnicon__gYE7n"]'))).click()
     
     chrome_wait.until(EC.visibility_of_element_located((By.XPATH,
          '//a[@class="BurgerMenu_container__item__08KwW"][1]'))).click()

     chrome_wait.until(lambda driver: '/applicant/account' in driver.current_url)
     assert '/applicant/account' in chrome.current_url
     
     cookies = chrome.get_cookies()
     with open("cookies.pkl", "wb") as file:
          pickle.dump(cookies, file)
