def int_func(words):
    result = []
    for elem in words:
        elem = chr(ord(elem[0]) - ord('a') + ord('A')) + elem[1:]
        result.append(elem)
    return ' '.join(result)


user_input = input('Введите строку: ').split()
print(int_func(user_input))
