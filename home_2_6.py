#  функция проверки введенного числа - вещественное оно или нет
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


goods_list = list()
goods_dict = {}
count = 1
menu = '1. Ввести данные о товаре\n2. Вывести данные о товарах\n3. Выход'

# заполняем список товаров и работаем с ним
while True:

    print(menu)
    change = input('Выберите пункт меню: ')

    if change == '1':

        goods_name = input('Введите наименование товара: ')
        while True:
            goods_price = (input('Укажите стоимость товара: '))
            if is_float(goods_price):
                goods_price = float(goods_price)
                break
            else:
                print('Вы ввели не число')

        while True:
            goods_amount = (input('Введите количество товара: '))
            if is_float(goods_amount):
                goods_amount = float(goods_amount)
                break
            else:
                print('Вы ввели не число')

        goods_unit = input('Укажите единицы измерения: ')

        #  заносим данные в словарь
        product_dict = {
            'название': goods_name,
            'цена': goods_price,
            'количество': goods_amount,
            'ед.измерения': goods_unit
        }
        #  в кортеж добавляем номер товара и словарь с параметрами
        goods = (count, product_dict)

        #  в список добавляем полученный кортеж
        goods_list.append(goods)
        count += 1

    elif change == '2':
        analytics_dict = {}
        # "извлекаем" данные из словарей. используем множества
        for elem in goods_list:
            for key, val in elem[1].items():
                analytics_dict.setdefault(key, set())
                analytics_dict[key].add(val)

        #  по заданию нужны списки - преобразуем
        for key, val in analytics_dict.items():
            analytics_dict[key] = list(analytics_dict[key])

        print('\nВ нашей базе "Товары" содержатся следующие элементы:')
        for key, value in analytics_dict.items(): print(f'"{key}": {value}')

    elif change == '3':
        print('Сеанс завершен. Всех благ!')
        break

    else:
        print('Повторите ввод!')
