import pytest
from utils.driver_setup import get_chrome


@pytest.fixture(scope="function")
def driver():
    driver = get_chrome()
    yield driver
    driver.quit()

