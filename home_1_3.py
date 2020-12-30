# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

num = input('Введите число: ')
summa = 0
count = 1

while count <= 3:
    summa += int(num * count)
    count += 1

print(summa)
