from utils.config import Config
from pages_ui.base_page import BasePage
from utils.locators import AuthPageLocators, AddFavorites, PersonalAccount, DeleteApplicant


class RegistrApplicant(BasePage):
    """Класс регистрации соискателя"""
    

class AuthorizationPage(BasePage):
    """Класс авторизации пользователя"""
    def open_login_form(self, email, password):
        """Класс авториции соискателя"""
        self.open(Config.BASE_URL)
        self.find(AuthPageLocators.auth_button).click()
        self.find(AuthPageLocators.email_field).send_keys(email)
        self.find(AuthPageLocators.password_field).send_keys(password)
        self.find(AuthPageLocators.submit_button).click()
        self.find(AuthPageLocators.account).click()
        self.find(AuthPageLocators.account_link).click()
        email_acc = self.find(
            PersonalAccount.email_account).get_attribute('value')
        return email_acc


class FavoritesPage(BasePage):
    """Класс для добавления вакансий в избранное"""
    def add_fav_vacancies(self):
        """Добавить первую вакансию из списка в избранное"""
        self.open(Config.BASE_URL)
        self.clear_cookies()
        self.load_user_cookies(1)
        self.driver.refresh()
        self.find(AddFavorites.first_vacancies).click()
        self.find(AddFavorites.add_fav).click()
        self.find(AddFavorites.open_fav_page).click()
        fav_vac = self.find_elements(AddFavorites.count_fav_vacancies)
        return fav_vac


class AccountPage(BasePage):
    """Класс для взаимодействия со страницей соискателя"""
    def account_email(self):
        """Валидация пользователя по его почте"""
        self.open(Config.BASE_URL)
        self.clear_cookies()
        self.load_user_cookies(1)
        self.open(Config.account_url)
        email_acc = self.find(
            PersonalAccount.email_account).get_attribute('value')
        return email_acc


class DeleteAppl(BasePage):
    """Класс для удаления аккаунта"""
    def dell_acc_appl(self) -> bool:
        """Удалить аккаунт соискателя"""
        self.open(Config.BASE_URL)
        self.clear_cookies()
        self.load_user_cookies(1)
        self.open(Config.account_url)
        self.find(DeleteApplicant.del_button_acc).click()
        self.find(DeleteApplicant.pass_appl).send_keys(Config.my_appl_pas_1)
        self.find(DeleteApplicant.check_box).click()
        self.find(DeleteApplicant.button_confirm_del).click()
        info_result = self.find_text(DeleteApplicant.info_del_appl, "Ваш аккаунт удалён")
        return info_result
