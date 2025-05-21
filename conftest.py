import os
import pytest
from utils.driver_setup import get_driver


@pytest.fixture(scope="function")
def driver():
    browser = os.getenv("BROWSER", "chrome").lower()
    driver_instance = get_driver(browser)
    yield driver_instance
    driver_instance.quit()

