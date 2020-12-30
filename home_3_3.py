def my_func(num_1, num_2, num_3):
    num_list = [num_1, num_2, num_3]
    num_list.sort()
    return num_list[-1] + num_list[-2]


entered_num = []
for i in range(3):
    while True:
        user_input = input('Введите число: ')
        if user_input.isdigit():
            entered_num.append(int(user_input))
            break
        else:
            print('Некорректный ввод!')

result = my_func(*entered_num)
print('_'*36)
print(f'Сумма двух наибольших чисел: {result}')
