# Реализовать базовый класс Worker (работник), в котором определить
# атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса
# Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {
            "wage": self.wage,
            "bonus": self.bonus
        }


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        Worker.__init__(self, name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


with open('home_6_3.txt', encoding='utf-8', errors='ignore') as file:
    worker_list = list(line.split() for line in file)

for elem in worker_list:
    for j in range(len(elem)):
        if elem[j].isdigit():
            elem[j] = int(elem[j])
    worker = Position(*elem)
    print(f'Имя, Фамилия сотрудника: {worker.get_full_name()}')
    print(f'Должность: {worker.position}')
    print(f'Доход с учётом премии: {worker.get_total_income()} у.е.')
    print('-' * 10)

# worker_1 = Position('Ivan', 'Ivanov', 'director', 21000, 12000)
# worker_2 = Position('Sergey', 'Petrov', 'engineer', 17000, 10000)
#
# print(worker_1.get_full_name())
# print(f'Доход с учётом премии: {worker_1.get_total_income()} у.е.')
#
