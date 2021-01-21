# Создать класс TrafficLight (светофор) и определить у него один атрибут color(цвет)
# и метод running (запуск). Атрибут реализовать как приватный. В рамках метода
# реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый)
# — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
# выводить соответствующее сообщение и завершать скрипт.
from time import sleep


class TrafficLight:

    __color = ['красный', 'желтый', 'зеленый']

    def __init__(self):
        self.green_time = 20
        self.yellow_time = 2
        self.red_time = 7
        self.work_cycle = 1

    def running(self):
        for i in range(self.work_cycle):
            print("\033[31m {}".format(TrafficLight.__color[0]))
            sleep(self.red_time)
            print("\033[33m {}".format(TrafficLight.__color[1]))
            sleep(self.yellow_time)
            print("\033[32m {}".format(TrafficLight.__color[2]))
            sleep(self.green_time)


lighter_1 = TrafficLight()
# запускаем с условиями по умолчанию
lighter_1.running()

# запускаем с условиями, нужными пользователю
print(f'\033[30m'
      f'Добро пожаловать в систему управления светофорным объектом.')
while True:
    print(f'Укажите время работы режимов светофора:')
    lighter_1.red_time = int(input(' красный: '))
    lighter_1.yellow_time = int(input(' жёлтый: '))
    lighter_1.green_time = int(input(' зеленый: '))
    lighter_1.work_cycle = int(input('Укажите количество циклов работы светофора: '))
    choice = input('Проверьте введённые данные. Нажмите "1" если всё верно или "0" если что-то нужно исправить: ')
    if choice == '1':
        break
print('Запускаем светофор!!!')
lighter_1.running()
print('\033[31m Светофор выключен!!!')
