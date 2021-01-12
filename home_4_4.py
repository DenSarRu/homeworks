# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]
from random import randrange

# заполним список случайными значениями
original_list = [randrange(1, 99, 2) for i in range(100)]
print(f'Исходный список: {original_list}')

new_list = [elem for elem in original_list if original_list.count(elem) == 1]

print(f'Решение задачи через подсчёт количества элементов:')
print(f'Новый список: {new_list}')

# или сложнее - через срезы
# original_list = [randrange(1, 99, 2) for j in range(100)]
new_list = [elem for num, elem in enumerate(original_list) if elem not in original_list[num + 1:]
            and elem not in original_list[:num]]
print(f'Решение задачи через срезы:')
print(f'Новый список: {new_list}')
