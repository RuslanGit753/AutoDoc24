from utils.config import ConfigAppl
from pages_ui.base_page import BasePage
from utils.locators import (AuthPageLoc, AddFavLoc,
                            PersAccLoc, DelApplLoc, RegistAppltLoc,
                            ResVacLoc)
from utils.gener_data import ApplTestData


class RegistrApplPage(BasePage):
    """Класс регистрации соискателя"""
    def open_form_regist_appl(self):
        """Открытие формы регистрации соискателя"""
        self.open(ConfigAppl.BASE_URL)
        self.find(RegistAppltLoc.auth_button).click()
        self.find(RegistAppltLoc.regis_betton).click()
        self.find(RegistAppltLoc.radio_job).click()
        self.find(RegistAppltLoc.next_button).click()

    def send_data_appl(self, first_name, last_name, mail, password):
        """Шаг первый: заполнение данных для регистрации"""
        self.find(RegistAppltLoc.first_name).send_keys(first_name)
        self.find(RegistAppltLoc.last_name).send_keys(last_name)
        self.find(RegistAppltLoc.mail).send_keys(mail)
        self.find(RegistAppltLoc.password).send_keys(password)
        self.find(RegistAppltLoc.regis_betton2).click()

    def send_code(self):
        """Шаг второй: ввести 4-x значный код подтверждения"""
        info_result = self.find_text(RegistAppltLoc.result_text,
                                     "Регистрация завершена", timeout=60)
        return info_result


class AuthorizationPage(BasePage):
    """Класс авторизации пользователя"""
    def open_login_form(self, email, password):
        """Заполнение формы авторизации: почта и пароль"""
        self.open(ConfigAppl.BASE_URL)
        self.find(AuthPageLoc.auth_button).click()
        self.find(AuthPageLoc.email_field).send_keys(email)
        self.find(AuthPageLoc.password_field).send_keys(password)
        self.find(AuthPageLoc.submit_button).click()

    def open_acc_appl(self):
        """Открытие личного кабинета и валидация почты соискателя"""
        self.find(AuthPageLoc.account).click()
        self.find(AuthPageLoc.account_link).click()
        email_acc = self.find(
            PersAccLoc.email_account).get_attribute('value')
        return email_acc


class FavoritesPage(BasePage):
    """Класс для добавления вакансий в избранное"""
    def load_cookies(self):
        """Загрузка кук авторизации пользователя"""
        self.open(ConfigAppl.BASE_URL)
        self.clear_cookies()
        self.load_user_cookies(1)
        self.driver.refresh()

    def add_fav_vacancies(self):
        """Добавить первую вакансию из списка в избранное"""    
        self.find(AddFavLoc.first_vacancies).click()
        self.find(AddFavLoc.add_fav).click()

    def check_vacan_fav(self):
        """Проверить вакансию на странице 'Избранное'"""
        self.find(AddFavLoc.open_fav_page).click()
        fav_vac = self.find_elements(AddFavLoc.count_fav_vacancies)
        return fav_vac


class DeleteApplPage(BasePage):
    """Класс для удаления аккаунта"""
    def load_cook_user(self) -> bool:
        """Загрузка кук авторизации пользователя"""
        self.open(ConfigAppl.BASE_URL)
        self.clear_cookies()
        self.load_user_cookies(1)
        self.driver.refresh()

    def dell_acc_appl(self, password):
        """Удаление аккаунта соискателя"""
        self.open(ConfigAppl.acc_appl_url)
        self.find(DelApplLoc.del_button_acc).click()
        self.find(DelApplLoc.pass_appl).send_keys(password)
        self.find(DelApplLoc.check_box).click()
        self.find(DelApplLoc.button_confirm_del).click()
        info_result = self.find_text(DelApplLoc.info_del_appl,
                                     "Ваш аккаунт удалён")
        return info_result


class ResVacPage(BasePage):
    """Класс для отклика на вакансию"""
    def load_cookies(self):
        """Загрузка кук авторизации пользователя"""
        self.open(ConfigAppl.BASE_URL)
        self.clear_cookies()
        self.load_user_cookies(1)
        self.driver.refresh()

    def respond_vac(self):
        """Откликнуться на первую вакансию из списка"""
        self.find(ResVacLoc.list_vac).click()
        title_posit = self.find(ResVacLoc.title_posit).text
        self.find(ResVacLoc.respond_button1).click()
        self.find(ResVacLoc.respond_button2).click()
        return title_posit

    def open_chat(self):
        """Открыть час с работодателем"""
        self.find(ResVacLoc.open_chat).click()
        self.find(ResVacLoc.open_vac_chat).click()
        title_posit_chat = self.find(ResVacLoc.title_posit_chat).text
        return title_posit_chat


class AddInfoApplPage(BasePage):
    """Класс добавления информации соискателя"""
    def load_cookies(self):
        """Загрузка кук авторизации пользователя"""
        self.open(ConfigAppl.BASE_URL)
        self.clear_cookies()
        self.load_user_cookies(1)
        self.driver.refresh()

    def add_phone(self, appl_phone):
        """Добавление номера телефона в личном кабинете"""
        self.open(ConfigAppl.acc_appl_url)
        self.find(PersAccLoc.phone).send_keys(appl_phone)
        self.find(PersAccLoc.submit_save).click()
        self.driver.refresh()

    def save_add_phone(self):
        """Сохранение добавленного номера"""
        save_phone = self.find(
            PersAccLoc.phone).get_attribute('value')
        return save_phone


class UpdInfoApplPage(BasePage):
    """Класс обновления информации соискателя"""
    def load_cookies(self):
        """Загрузка кук авторизации пользователя"""
        self.open(ConfigAppl.BASE_URL)
        self.clear_cookies()
        self.load_user_cookies(1)
        self.driver.refresh()

    def get_old_phone(self):
        """Проверка наличия номера в поле"""
        self.open(ConfigAppl.acc_appl_url)
        old_phone = self.find(
            PersAccLoc.phone).get_attribute('value')
        return old_phone

    def add_new_phone(self, new_phone):
        """Заменить старый номер на новый"""
        self.find(PersAccLoc.phone).send_keys(new_phone)
        self.find(PersAccLoc.submit_save).click()
        self.driver.refresh()

    def save_new_phone(self):
        """Записать длбавленный номер в переменную"""
        new_phone = self.find(
            PersAccLoc.phone).get_attribute('value')
        return new_phone
