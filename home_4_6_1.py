# Реализовать итератор, генерирующий целые числа, начиная с указанного,
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения:
# выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
from itertools import count
performance = True
while performance:
    start_num = input('Введите начальное значение: ')
    element_num = input('Введите требуемое количество элементов: ')
    try:
        start_num = int(start_num)
        element_num = int(element_num)
        for elem in count(start_num):
            if elem == start_num + element_num:
                performance = False
                break
            else:
                print(elem)
    except ValueError:
        print('Ошибка ввода...')
        continue
