# Реализовать скрипт:
# итератор, повторяющий элементы некоторого списка, определенного заранее.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
from itertools import cycle

original_list = [elem for elem in 'https://geekbrains.ru/']
# print(original_list)
counter = 0
for elem in cycle(original_list):
    if counter > 24:
        break
    else:
        print(elem)
    counter += 1
