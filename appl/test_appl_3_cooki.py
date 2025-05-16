from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from conftest import username_value, password_value, chrome_wait, chrome


chrome_wait.until(EC.visibility_of_element_located((
By.XPATH, '//button[@class="Header_header__authorized__l3dJL"]'))).click()
        
email = chrome_wait.until(EC.visibility_of_element_located((
By.XPATH, '//input[@type="email"]')))
email.send_keys(username_value)

password = chrome_wait.until(EC.visibility_of_element_located((
By.XPATH, '//input[@type="password"]')))
password.send_keys(password_value)

chrome_wait.until(EC.visibility_of_element_located((
By.XPATH, '//button[@type="submit"]'))).click()

account = chrome_wait.until(EC.visibility_of_element_located((
By.XPATH, '//div/div/button[@class="Icons_btnicon__gYE7n"]')))
account.click()
     
tatle = chrome.title
print(tatle)

