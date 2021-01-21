# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
menu = '1. Создать файл и записать в него набор чисел\n2. Вывести данные\n3. Выход'
while True:
    print(menu)
    choice = input('Выберите пункт меню: ')

    if choice == '1':
        print('Вводите числа. Для окончания ввода чисел нажмите "q"!')
        row = ''
        while True:
            user_input = input('Введите число: ')
            if user_input.lower() == 'q':
                break
            if user_input.isdigit():
                row += user_input + ' '
            if not user_input.isdigit():
                print('Вы ошиблись с вводом. Вводите числа. Для окончания ввода чисел нажмите "q"!!!')
        print(f'Вы ввели такие числа: {row}')
        print('Теперь мы создадим файл и запишем в него введенные числа.\n')
        with open('homework_5_5.txt', 'w') as file:
            file.write(row)

    elif choice == '2':
        try:
            with open('homework_5_5.txt') as file:
                line = file.read()
                print(f'В файле записаны следующие числа: {line}')
                summa = sum(int(item) for item in line.split())
                print(f'Сумма чисел в файле: {summa}')
        except FileNotFoundError:
            print('Файл пока не создан. Выберите пункт №1 и запишите в файл данные!!!')

    elif choice == '3':
        print('Сеанс завершен. Всего доброго!')
        break

    else:
        print('Повторите ввод!')


# print(sum(map(int, file.readline().split())))
