# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
# автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
from time import sleep
from random import choice


class Car:

    def __init__(self, color, name):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f'Ваша машина поехала.')

    def stop(self):
        print(f'Ваша машина остановилась.')

    def turn(self, direction):
        self.direction = direction
        if direction.lower() == 'left':
            print(f'Ваша машина повернула налево <---')
        elif direction.lower() == 'right':
            print(f'Ваша машина повернула направо --->')
        elif direction.lower() == 'straight':
            print(f'Ваша машина едет прямо ^')

    def show_speed(self, speed):
        print(f'Ваша текущая скорость {speed} км/ч')


class TownCar(Car):
    def __init__(self, color, name):
        Car.__init__(self, color, name)
        self.max_speed = 60

    def show_speed(self, speed):
        print(f'Ваша текущая скорость {speed} км/ч')
        if speed > 60:
            print(f'Ваша скорость выше 60 км/ч! '
                  f'Пожалуйста, снизьте скорость!!!')


class SportCar(Car):
    def __init__(self, color, name):
        Car.__init__(self, color, name)
        self.max_speed = 350


class WorkCar(Car):
    def __init__(self, color, name):
        Car.__init__(self, color, name)
        self.max_speed = 40

    def show_speed(self, speed):
        print(f'Ваша текущая скорость {speed} км/ч')
        if speed > 40:
            print(f'Ваша скорость выше 40 км/ч! '
                  f'Пожалуйста, снизьте скорость!!!')


class PoliceCar(Car):
    def __init__(self, color, name):
        Car.__init__(self, color, name)
        self.is_police = True


def car_creation():
    car_type_list = [TownCar, SportCar, WorkCar, PoliceCar]
    menu = ['1. Городская машина', '2. Спортивная машина', '3. Служебная машина', '4. Полицейский автомобиль']
    car_type_choice = input('Укажите тип машины ({}): '.format('; '.join(menu)))
    car_color = input('Какого цвета нужна машина: ')
    car_name = input('Какое название у этой машины: ')
    if car_type_choice == '1':
        return car_type_list[0](car_color, car_name)
    elif car_type_choice == '2':
        return car_type_list[1](car_color, car_name)
    elif car_type_choice == '3':
        return car_type_list[2](car_color, car_name)
    elif car_type_choice == '4':
        return car_type_list[3](car_color, car_name)


new_car = car_creation()
print(f'Вы выбрали машину с модным цветом: {new_car.color} и с шикарным именем "{new_car.name}".')

if new_car.is_police:
    print('Удачи на дежурстве товарищ полицейский!!! Пристегните ремни.')
    new_car.go()
    for i in range(10):
        car_direction = choice(['left', 'right'])
        new_car.turn(car_direction)
        sleep(2)
    new_car.stop()
else:
    car_speed = int(input('До какой скорости будем разгоняться: '))
    if car_speed > new_car.max_speed:
        print(f'Напоминаю, что максимальная скорость для вашего типа авто: {new_car.max_speed} км/час')
    new_car.go()
    now_car_speed = 1
    trip_time = 0
    while now_car_speed > 0:
        car_direction = choice(['left', 'right', 'straight'])
        new_car.turn(car_direction)
        if trip_time < 20:  # пока сделал искусственное ограничение времени движения
            if now_car_speed < car_speed:
                new_car.show_speed(now_car_speed)
                sleep(2)
                now_car_speed += 5

            elif now_car_speed == car_speed:
                new_car.show_speed(now_car_speed)
                sleep(2)

            else:
                new_car.show_speed(now_car_speed)
                now_car_speed -= 2
                sleep(2)
            trip_time += 1
        else:
            print('Предлагаю остановиться и сделать перерыв...')
            new_car.show_speed(now_car_speed)
            now_car_speed -= 10
            sleep(2)
    new_car.stop()
