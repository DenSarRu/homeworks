# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

num = input('Введите целое положительное число: ')

count = 0
max_number = 0

while count < len(num):
    i = (int(num) // (10**count) % 10)
    if i <= max_number:
        count += 1
        continue
    max_number = i
    count += 1

print('В числе {} самая большая цифра {}'.format(num, max_number))
