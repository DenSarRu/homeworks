# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
from random import choice

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки...')


class Pen(Stationery):
    def __init__(self, title):
        Stationery.__init__(self, title)

    def draw(self):
        return 'Начинаем рисовать ручкой.'


class Pencil(Stationery):
    def __init__(self, title):
        Stationery.__init__(self, title)

    def draw(self):
        return 'Начинаем рисовать карандашом.'


class Handle(Stationery):
    def __init__(self, title):
        Stationery.__init__(self, title)

    def draw(self):
        return 'Начинаем рисовать маркером.'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(f'Если в руке {pen.title}, то {pen.draw()}')
print(f'Оказался у нас {pencil.title}, то {pencil.draw()}')
print(f'Ну а если, случайно или нет, вы взяли {handle.title}, то {handle.draw()}')
