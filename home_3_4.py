def my_func(x, y):
    return x ** y


def my_func_2(x, y):
    res = 1
    for i in range (1,abs(y)+1):
        res *= 1/x
    return res


num_1 = int(input('Введите положительное число: '))
num_2 = int(input('Введите целое отрицательное число: '))
result_1 = my_func(num_1, num_2)
result_2 = my_func_2(num_1, num_2)

print('-'*30)
print(f'Результат возведения в степень с помощью оператора **: {result_1}\n'
      f'Результат возведения в степень без оператора **, с использование цикла: {result_2}')
