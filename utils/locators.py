from selenium.webdriver.common.by import By

class AuthPageLocators:
        auth_button = (By.XPATH, '//button[@class="Header_header__authorized__l3dJL"]')
        email_field = (By.XPATH, '//input[@type="email"]')
        password_field = (By.XPATH, '//input[@type="password"]')
        submit_button = (By.XPATH, '//button[@type="submit"]')
        account = (By.XPATH, '//button/img[@alt="Account"]')
        account_link = (By.XPATH, '//a[@class="BurgerMenu_container__item__08KwW"][1]')

class PersonalAccount:
        email_account = (By.CSS_SELECTOR, '#email')