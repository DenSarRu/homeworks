seasons_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}

month_num = input('Введите номер месяца (от 1 до 12): ')

while True:
    if month_num.isdigit() and 1 <= int(month_num) <= 12:
        month_num = int(month_num)
        break
    else:
        print('Не совсем правильный ввод...')
        month_num = input('Введите номер месяца (число от 1 до 12): ')

if month_num == 12 or 1 <= month_num <= 2:
    print(seasons_dict.get(1), '!.. Крестьянин, торжествуя, На дровнях обновляет путь \n')

elif 3 <= month_num <= 5:
    print('К нам', seasons_dict.get(2), 'шагает быстрыми шагами')

elif 6 <= month_num <= 8:
    print('Вот оно какое наше', seasons_dict.get(3))

elif 9 <= month_num <= 11:
    print('Миновало лето, \n', seasons_dict.get(4), 'наступила...\n')
