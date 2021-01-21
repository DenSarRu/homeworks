# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
import json

firm_list = []
firm_dict = {}
profit_dict = {}
profit_firm_counter = 0
average_profit = 0

with open('homework_5_7.txt', encoding='utf-8', errors='ignore') as file:
    for line in file:
        firm, form, proceeds, costs = line.split()
        profit = int(proceeds) - int(costs)
        firm_dict[firm] = profit
        if profit > 0:
            average_profit += profit
            profit_firm_counter += 1
    try:
        average_profit /= profit_firm_counter
    except ZeroDivisionError:
        print('К сожалению все указанные предприятия убыточны...')

    profit_dict['average_profit'] = average_profit
    firm_list.append(firm_dict)
    firm_list.append(profit_dict)
    print(f'Прибыль компаний и средняя прибыль:\n{firm_list}')

with open('homework_5_7_out.json', 'w') as out_file:
    json.dump(firm_list, out_file)

with open('homework_5_7_out.json') as inf:
    data_new = json.load(inf)
print(f'В результате работы был создан файл json со следующим содержимым:\n{data_new}')
