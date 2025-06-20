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


class AddResume:
        but_add_resume = (By.CSS_SELECTOR, '.HeaderButton_btn__phhYC')
        job_title = (By.CSS_SELECTOR, '#job_title')
        wages = (By.CSS_SELECTOR, '.FormInput_inputCustom__23Prn')
        """
        График работы
        """
        chart_full = (By.XPATH, '//label[@for="schedule-0"]')
        chart_flexible = (By.XPATH, '//label[@for="schedule-1"]')
        chart_remote = (By.XPATH, '//label[@for="schedule-2"]')
        chart_removable = (By.XPATH, '//label[@for="schedule-3"]')
        chart_watch = (By.XPATH, '//label[@for="schedule-4"]')
        """
        Формат работы
        """
        format_full = (By.XPATH, '//label[@for="work_format-0"]')
        format_partial = (By.XPATH, '//label[@for="work_format-1"]')
        format_internship = (By.XPATH, '//label[@for="work_format-2"]')
        format_project = (By.XPATH, '//label[@for="work_format-3"]')
        nex_one_but = (By.CSS_SELECTOR, '.FormButton_next__hj6Gi')
        """
        Основная информация
        """
        add_avatar = (By.XPATH, '//input[@name="ResumePhoto"]')
        first_name = (By.CSS_SELECTOR, '#first_name')
        last_name = (By.CSS_SELECTOR, '#last_name')
        sex_group_female = (By.XPATH, '//input[@value="FEMALE"]')
        sex_group_male = (By.XPATH, '//input[@value="MALE"]')
        birth_day = (By.CSS_SELECTOR, '.FormDate_day__oIE3W')
        birth_month = (By.CSS_SELECTOR, '.FormDate_month__1QwZ7')
        birth_year = (By.CSS_SELECTOR, '.FormDate_year__KuVO7')
        city = (By.CSS_SELECTOR, '#city')
        phone = (By.CSS_SELECTOR, '#tel')
        nex_two_but = (By.CSS_SELECTOR, '.FormButton_next__hj6Gi')
        """
        Опыт работы
        """
        chekbox_no_experience = nex_two_but = (By.CSS_SELECTOR, '#experience-0')
        period_start_month = (By.XPATH, '//div[1]/div[1]/div[1][text()="Месяц"]')
        month_jun = (By.XPATH, '//div[@id="5"]') # По умолчанию июнь


        period_start_year = (By.XPATH, '')
        
        company_name = (By.CSS_SELECTOR, '#company_name_0')
        profession_name = (By.CSS_SELECTOR, '#profession_0')
        duties = (By.CSS_SELECTOR, '#responsibility_0')
        achievements = (By.CSS_SELECTOR, '#achievements_0')

        nex_three_but = (By.CSS_SELECTOR, '.FormButton_next__hj6Gi')
        """
        Образование
        """
        # Уровень образования
        level_midle = (By.XPATH, '//label[@for="education_level-0-0"]')
        level_midle_special = (By.XPATH, '//label[@for="education_level-0-1"]')
        level_high = (By.XPATH, '//label[@for="education_level-0-2"]')
        level_none = (By.XPATH, '//label[@for="education_level-0-3"]')

        educ_institut = (By.XPATH, '//input[@name="institute_name"]')
        faculty = (By.XPATH, '//input[@name="faculty"]')
        profession = (By.XPATH, '//input[@name="profession"]')
        button_end_year = (By.CSS_SELECTOR, '#education_end_year-0')
        educ_end_year = (By.XPATH, '//div[@id="15"]') # По умолчанию 2020
        nex_four_but = (By.CSS_SELECTOR, '.FormButton_next__hj6Gi')
        """
        Дополнительно 
        """
        # Язык
        but_language = (By.CSS_SELECTOR, '#language-0')
        language = (By.XPATH, '//div[@id="0"]') # По умолчанию Русский
        but_language_level = (By.CSS_SELECTOR, '#language_level-0') 
        language_level = (By.XPATH, '//div[@id="4"]') # По умолчанию родной

        # Повышение квалификации и курсы
        dop_institute_name = (By.CSS_SELECTOR, '#institute_name-0')
        dop_faculty = (By.CSS_SELECTOR, '#faculty-0')
        dop_profession = (By.CSS_SELECTOR, '#profession-0')
        dop_but_year_end = (By.CSS_SELECTOR, '.Additional_year__box__ag_ua')
        dop_year_end = (By.XPATH, '//div[@id="12"]') # По умолчанию 2023
        dop_certificate = (By.XPATH, '//button[text()="Прикрепить сертификат"]')
        dop_addCourseButton = (By.CSS_SELECTOR, '#addCourseButton')

        # Портфолио
        portf_link = (By.CSS_SELECTOR, '//button[text()="Файл"]')
        portf_add_file = (By.XPATH, '//button[text()="Файл"]')
        portf_description = (By.CSS_SELECTOR, '#portfolio-description-0')
        portf_add = (By.CSS_SELECTOR, '#addPortfolioButton')
        nex_five_but = (By.CSS_SELECTOR, '.FormButton_next__hj6Gi')
        """
        О себе
        """
        personal_info = (By.CSS_SELECTOR, '.PersonalInfo_textarea__fSkAz')
        form_button_publish = (By.CSS_SELECTOR, '.FormButton_publish__Mbvoo') # Опубликовать 


class AddFavorites:
        first_vacancies = (By.CSS_SELECTOR, '.EmployerCard_card__AY0Jq') # По умолчанию первая вакансия в списке
        add_fav = (By.CSS_SELECTOR, '[class*="like__fts2F"]')
        open_fav_page = (By.CSS_SELECTOR, '.Icons_fav__2LNv5')
        count_fav_vacancies = (By.CSS_SELECTOR, '.EmployerCard_card__AY0Jq') # Отображает количество добавленных вакансий
