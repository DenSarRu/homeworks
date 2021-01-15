def division(div_1, div_2):
    try:
        div_1 = int(div_1)
        div_2 = int(div_2)
    except ValueError:
        return 'Вы ввели некорректное значение...'
    return 'На ноль делить нельзя!!' if div_2 == 0 else f'Результат деления: {div_1 / div_2}'


num_1 = input('Введите делитель: ')
num_2 = input('Введите делимое: ')

print(division(num_1, num_2))
