# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1/Two — 2/Three — 3/Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны заменяться на
rus_dict = {
    '1': 'один',
    '2': 'два',
    '3': 'три',
    '4': 'четыре',
    '5': 'пять',
    '6': 'шесть',
    '7': 'семь',
    '8': 'восемь',
    '9': 'девять',
    '0': 'ноль'
}

with open('homework_5_4.txt', encoding='utf-8', errors='ignore') as inf, \
        open('homework_5_4_out.txt', 'w', encoding='utf-8', errors='ignore') as out:
    for line in inf:
        row = line.split()
        row[0] = rus_dict[line.split()[-1]]
        out.write(' '.join(row) + '\n')
