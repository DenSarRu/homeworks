from time import sleep


class Cell:
    """
    Класс для работы с органическими клетками
    """
    def __init__(self, num):
        """ num - определяет количество клеток """
        self.cell_number = num

    def __add__(self, other):
        """ сложение клеток
        Выполняет объединение двух клеток.
        Число ячеек общей клетки равняется сумме ячеек исходных двух клеток.
        """
        return self.cell_number + other.cell_number

    def __sub__(self, other):
        """  вычитание клеток
        Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
        больше нуля, иначе выводить соответствующее сообщение.
        """
        try:
            if self.cell_number - other.cell_number < 0:
                raise ArithmeticError
        except ArithmeticError:
            return 'Вычитание невозможно!'
        else:
            return self.cell_number - other.cell_number

    def __mul__(self, other):
        """ умножение клеток
        Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
        """
        return self.cell_number * other.cell_number

    def __truediv__(self, other):
        """
        Метод деления клеток. В этом методе осуществляется округление значения до целого числа.
        """
        return round(self.cell_number / other.cell_number)

    def make_order(self, count: int) -> str:
        """
        Метод позволяет организовать ячейки по рядам.
        self - экземпляр класса
        count - количество ячеек в ряду
        """
        row = ''
        for i in range(int(self.cell_number / count)):
            row += f'{"*" * count}\n'
        row += f'{"*" * (self.cell_number % count)}'
        return row


cell_1 = Cell(int(input('Укажите число ячеек первой клетки: ')))
cell_2 = Cell(int(input('Укажите число ячеек второй клетки: ')))
print(f'Результат сложения двух клеток: {cell_1 + cell_2}')
sleep(3)
print(f'Результат вычитания двух клеток: {cell_1 - cell_2}')
sleep(3)
print(f'Результат умножения двух клеток: {cell_1 * cell_2}')
sleep(3)
print(f'Результат деления двух клеток: {cell_1 / cell_2}')

print(f'Результат работы метода make_order:\n{cell_1.make_order(3)}')
print(f'Результат работы метода make_order:\n{cell_2.make_order(3)}')
print(f'Результат работы метода make_order:\n{cell_2.make_order(5)}')
