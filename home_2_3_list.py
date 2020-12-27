seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']

month_num = input('Введите номер месяца (от 1 до 12): ')

while True:
    if month_num.isdigit() and 1 <= int(month_num) <= 12:
        month_num = int(month_num)
        break
    else:
        print('Не совсем правильный ввод...')
        month_num = input('Введите номер месяца (число от 1 до 12): ')

if month_num == 12 or 1 <= month_num <= 2:
    print('Поет', seasons_list[0], ' — аукает,\nМохнатый лес баюкает')
elif 3 <= month_num <= 5:
    print('К нам', seasons_list[1], 'шагает быстрыми шагами')
elif 6 <= month_num <= 8:
    print('Вот оно какое наше', seasons_list[2])
elif 9 <= month_num <= 11:
    print(seasons_list[3], 'наступила,\nВысохли цветы...')
