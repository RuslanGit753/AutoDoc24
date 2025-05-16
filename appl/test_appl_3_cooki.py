import pickle
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def test_filter(chrome_wait, chrome):
    cookies = pickle.load(open("cookies.pkl", "rb"))

    for cookie in cookies:
        chrome.add_cookie(cookie)

    chrome_wait.until(EC.visibility_of_element_located((
    By.CSS_SELECTOR, '.Filter_filter__search__N__0c'))).click()
    time.sleep(5)

