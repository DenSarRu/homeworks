# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
# платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

# --------------------------------------
# from sys import argv
# script_name, output_in_hours, rate_per_hour, premium = argv
# try:
#     output_in_hours = int(output_in_hours)
#     rate_per_hour = int(rate_per_hour)
#     premium = int(premium)
#     salary = output_in_hours * rate_per_hour + premium
#     print(f'Заработная плата сотрудника: {salary} теньге.')
# except ValueError:
#     print('Not a number')
# --------------------------------------
def salary():
    try:
        output_in_hours = float(input('Выработка работника в часах: '))
        rate_per_hour = int(input('Ставка работника (у.е.): '))
        premium = int(input('Премия работника (у.е.) '))
        work_salary = output_in_hours * rate_per_hour + premium
        print(f'Заработная плата сотрудника: {work_salary} у.е.')
    except ValueError:
        return print('Not a number')


salary()
