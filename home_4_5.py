# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
from functools import reduce


def my_func(prev, element):
    return prev * element


original_list = [elem for elem in range(100, 1001, 2)]
print(f'Исходный список четных значений от 100 до 1000:\n{original_list}')
print(f'Произведение всех элементов списка:\n{reduce(my_func, original_list)}')

print(reduce(lambda a, b: a * b, [x for x in range(100, 1001, 2)]))

