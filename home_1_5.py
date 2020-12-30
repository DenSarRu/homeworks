# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

proceeds = float(input('Укажите размер выручки предприятия: '))
costs = float(input('Укажите размер издержек предприятия: '))
fin_result = proceeds - costs

if fin_result > 0:
    print('Поздравляю! Ваше предприятие приносит прибыль!')
    print('Рентабельность выручки вашей фирмы: {:.2%}'.format(fin_result/proceeds))
    num_of_employees = int(input('Укажите численность сотрудников фирмы: '))
    print('Прибыль фирмы в расчете на одного сотрудника составляет: {:.3f} у.е.'.format(fin_result/num_of_employees))

elif fin_result == 0:
    print('Прибыли нет... но и убытков тоже. Значит нужно еще поднажать!')

else:
    print('Убытки... Вероятно надо сократить издержки. Может уволим садовника?')
