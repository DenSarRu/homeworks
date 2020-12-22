start_result = int(input('Укажите результат пробежки в первый день: '))
fin_result = int(input('Укажите жалаемый результат: '))

daily_result = start_result
day_of_training = 1

print('\nРезультат:\n{}-й день: {:.2f} км'.format(day_of_training, daily_result))

while daily_result < fin_result:
    daily_result *= 1.1
    day_of_training += 1
    print('{}-й день: {:.2f} км'.format(day_of_training, daily_result))

print('\nНа {}-й день спортсмен достигнет результата — не менее {} км.'.format(day_of_training, fin_result))
