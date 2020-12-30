list_test = []

print('Давайте создадим список!')

while True:
    row = input("Напишите что-нибудь - число, слово и т.д. Для окончания введите 'q': ")
    if row.lower() == 'q':
        break
    list_test.append(row)


for i in range(0, len(list_test)-1, 2):
    list_test[i], list_test[i+1] = list_test[i+1], list_test[i]

print(list_test)
