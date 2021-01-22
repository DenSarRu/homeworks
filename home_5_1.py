# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
# with open('homework_5_1.txt', 'a') as file:
#     while True:
#         row = input('Введите данные: ')
#         if len(row) != 0:
#             file.write(row + '\n')
#         else:
#             break
#
# with open('homework_5_1.txt') as file:
#     print(f'Получившийся файл:\n{file.read()}')


with open('homework_5_1.txt', 'w+') as file:
    while True:
        row = input('Введите данные: ')
        if len(row) != 0:
            file.write(row + '\n')
        else:
            break
    file.seek(0)
    print(f'Получившийся файл:\n{file.read()}')

