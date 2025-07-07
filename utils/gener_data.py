from faker import Faker

fake = Faker()

class ApplTestData:
    """Класс дял нгенерации тестовых данных соискателя"""

    # Номер телефона 
    tel_num = "+7 (356) 896 45 32"

    @staticmethod
    def gen_email():
        """Генерация почты"""
        return fake.email()

    def gen_letter() -> str:
        """Генерация 1 буквы"""
        return fake.random_letter()

    @staticmethod
    def gen_pas(length=5) -> int:
        """Генерация пароля из length символов,
        по умолчанию 5 символов
        """
        return fake.password(length=length)

    @staticmethod
    def gen_registr(upper_case=True) -> bool: 
        """Настройка регистра букв:
        True - генерация с участием верхнего регистра
        False - генерация только в нижнем регистре
        """
        return fake.password(length=10, upper_case=upper_case)

    @staticmethod
    def gen_spec_chars():
        """Генерация пароля без спецсимволов"""
        return fake.password(length=10, special_chars=False)

    @staticmethod
    def gen_non_num():
        """Генерация пароля без цифр"""
        return fake.password(length=10, digits=False)

    @staticmethod
    def gen_num(digits=5):
        """Генерация числа, по умолчании 5 знаков"""
        return fake.random_number(digits=digits)
