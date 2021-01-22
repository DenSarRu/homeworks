# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

# решаем проблему с косяками в виде пустых строк в файле...
with open('homework_5_3.txt', encoding='utf-8', errors='ignore') as inf, \
        open('homework_5_3_out.txt', 'w', encoding='utf-8', errors='ignore') as out:
    for line in inf:
        if not line.isspace():
            out.write(line)
# работаем с полученным файлом
# with open('homework_5_3_out.txt', encoding='utf-8', errors='ignore') as file:
#     lines = file.readlines()
#     salary_less_20 = []
#     average_salary = 0
#     for elem in lines:
#         if not elem.isspace():
#             if int(elem.split()[1]) < 20000:
#                 salary_less_20.append(elem.split()[0])
#             average_salary += int(elem.split()[1])
#     average_salary /= len(lines)
#     print(f'Общее количество сотрудников: {len(lines)} человек.')
#     print(f'Средняя величина дохода сотрудников: {average_salary}')
#     print(f'Сотрудников с окладом менее 20 тыс.: {len(salary_less_20)} человек')
#     print('Список этих сотрудников:\n{}'.format('\n'.join(salary_less_20)))


with open('homework_5_3_out.txt', 'r', encoding='utf-8') as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Average salary = {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
          f'Employees with salary less than 20k {[e[0] for e in employees_dict.items() if e[1] < 20000]}')