# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в
# виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
from datetime import datetime, date


class Date:
    def __init__(self, date_in_str: str):
        self.date = date_in_str

    @classmethod
    def get_date(cls, param: str) -> list:
        """
        метод извлекает число, месяц, год из строки, преобразовывает их тип к типу «Число» и помещает в список
        """
        return list(map(int, param.split('-')))

    @staticmethod
    def validate_the_date(enter_date):
        """
        меотод, проверяющий правильность ввода даты: число, месяц и год
        :return: возвращает результат проверки введённой даты
        """
        check_date = list(map(int, enter_date.split('-')))
        try:
            date(check_date[2], check_date[1], check_date[0])
            return 'Дата введена корректно'
        except ValueError:
            return 'Некорректный ввод даты'

    def __str__(self):
        return f'Текущая дата: {"/".join(map(str, Date.get_date(self.date)))}'


today_date = datetime.strftime(datetime.now(), '%d-%m-%Y')
today = Date(today_date)
print(today.date, type(today.date))
print(today)
print(Date.get_date(today_date))

entered_date = input('Введите дату в формате ДД-ММ-ГГГГ: ')
print(Date.validate_the_date(entered_date))
