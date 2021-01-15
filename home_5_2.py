# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
with open('homework_5_2.txt') as file:
    lines = file.readlines()
    print(f'Количество строк в файле: {len(lines)}')
    for num, line in enumerate(lines, 1):
        print(f'Количество слов в {num}й строке: {len(line.split())}')
