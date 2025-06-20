from pages.fav_appl_page import FavoritesPage
from utils.config import Config


def test_add_fav_vacancies(driver):
    page = FavoritesPage(driver)
    fav_vac = page.add_fav_vacancies()

    assert len(fav_vac) == 1