#  функция проверки введенного числа - вещественное оно или нет
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


list_test = [1980, 2020, 'GeekBrain', None, 'Tom and Jerry', 'Croods family', 'Wally', True, 123, 3.1415,
             ['Thor', 'Thor: The Dark World']]

print('У нас есть вот такой список:\n{}\nДавайте дополним список какими либо значениями!'.format(list_test))
print()

while True:
    row = input("Напишите что-нибудь - число, слово и т.д. Для выхода введите 'q': ")
    if row.isdigit():
        list_test.append(int(row))
    elif is_float(row):
        list_test.append(float(row))
    elif row.lower() == 'true':
        list_test.append(True)
    elif row.lower() == 'false':
        list_test.append(False)
    elif row.lower() == 'none':
        list_test.append(None)
    elif row.lower() == 'q':
        break
    else:
        list_test.append(row)

print()

for i in range(len(list_test)):
    print('Элемент списка "{}" относится к {}.'.format(list_test[i], type(list_test[i])))
