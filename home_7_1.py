from random import randint


class Matrix:
    """
    Класс Matrix (матрица).
    Принимает на вход данные (список списков) и формирует из них матрицу.
    """
    def __init__(self, arg):
        """ arg: список списков """
        self.matrix = arg

    def __str__(self):
        """ печатает матрицу в привычном виде """
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))

    def __add__(self, other):
        """ реализует операцию сложения двух матриц и возвращает новую матрицу """
        return Matrix([[el_1 + el_2 for el_1, el_2 in zip(self.matrix[i], other.matrix[i])]
                       for i in range(len(self.matrix))])


row = int(input('Укажите кол-во строк в матрице: '))
column = int(input('Укажите кол-во столбцов в матрице: '))
mat_1 = Matrix([[randint(0, 10) for j in range(column)] for i in range(row)])
mat_2 = Matrix([[randint(0, 10) for k in range(column)] for n in range(row)])
print('Матрица №1:\n{}\nМатрица №2:\n{}\n'.format(mat_1, mat_2))

mat_3 = mat_1 + mat_2
print('Сумма исходных матриц:\n{}'.format(mat_3))
