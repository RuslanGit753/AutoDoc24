from utils.config import Config
from pages.base_page import BasePage
from utils.locators import AddFavorites


class FavoritesPage(BasePage):
    def add_fav_vacancies(self):
        self.open(Config.BASE_URL)
        self.clear_cookies()
        self.load_user_cookies(1)
        self.driver.refresh()
        self.find(AddFavorites.first_vacancies).click()
        self.find(AddFavorites.add_fav).click()
        self.find(AddFavorites.open_fav_page).click()
        fav_vac = self.find_elements(AddFavorites.count_fav_vacancies)
        return fav_vac
