# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
# нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.

class MyZeroDevError(Exception):
    txt = 'Делитель равен нулю. Деление невозможно!!!'

    def __str__(self):
        return self.txt


class MyCalc:
    def __init__(self, num):
        self.num = num

    def __truediv__(self, other):
        try:
            if other.num == 0:
                raise MyZeroDevError
            return f'Результат деления: {self.num / other.num}'
        except MyZeroDevError as err:
            return err


num_1 = MyCalc(int(input('Введите делимое: ')))
num_2 = MyCalc(int(input('Введите делитель: ')))
print(num_1 / num_2)
