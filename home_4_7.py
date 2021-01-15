# Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
def fact(num):
    factorial = 1
    if num == 0:
        yield factorial
    else:
        for i in range(1, num + 1):
            factorial *= i
            yield factorial


user_input = input('Введите число: ')
try:
    user_input = int(user_input)
    for elem in fact(user_input):
        print(elem)
except ValueError:
    print('Нужно ввести число!!!')


# я понимаю, что в программу можно добавить сахарку и упростить ее вот так:
# from math import factorial
#
#
# def fact(num):
#     for i in range(1, num + 1):
#         yield factorial(i)
