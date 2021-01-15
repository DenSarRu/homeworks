def string_sum():
    current_status = True  # переменная для определения выхода или продолжеия
    result = 0

    while current_status:
        user_input = input('Введите числа, разделенные пробелом. Для завершения работы нажмите "Q":\n').split()

        for elem in user_input:
            if elem.upper() == 'Q':
                current_status = False
                break
            elif elem.isalpha():
                print('Некорректный ввод! Будьте внимательны - вводите числа или "Q". ')
            else:
                result += int(elem)
        print(f'Сумма всех введённых чисел: {result:<4}')


string_sum()
