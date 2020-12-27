row = input('Введите строку из нескольких слов, разделённых пробелами: ')

word_list = row.split()
for index, elem in enumerate(word_list):
    print(index, elem[0:10])
