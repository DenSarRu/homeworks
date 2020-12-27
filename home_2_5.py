rating_list = [7, 7, 5, 3, 3, 2]

print('Наш рейтинг: ', ', '.join(map(str, rating_list)))

#  теперь заносим новые элементы в список
while True:
    user_input = input('Введите новый элемент рейтинга. Для выхода нажмите "q": ')
    if user_input.lower() == 'q':
        break
    elif user_input.isalpha():
        print('Вы ошиблись. Нужно вводить только числа или "q" для выхода!')
        continue
    user_input = int(user_input)
#  Если в рейтинге существуют элементы с таким значением, то новый элемент с тем же значением разместится после них.
    if user_input in rating_list:
        new_index = rating_list.index(user_input) + rating_list.count(user_input) - 1
        rating_list.insert(new_index, user_input)
#  Максимаьный элемент - в начало...
    elif user_input > max(rating_list):
        rating_list.insert(0, user_input)
#  ... минимальный - в конец...
    elif user_input <= min(rating_list):
        rating_list.insert(len(rating_list), user_input)
#  ...ну а остальных будем сортировать
    else:
        for i in range(0, len(rating_list)-1):
            if rating_list[i+1] < user_input < rating_list[i]:
                rating_list.insert(i+1, user_input)

print('Новый рейтинг:')
print(', '.join(map(str, rating_list)))
