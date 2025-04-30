from selenium.webdriver.support import expected_conditions as EC



def test_open_browser(driver):
    assert driver.current_url == 'https://rabota.ktsf.ru/vacancies'


