# Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны
# передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см
# * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def square(self):
        return self._length * self._width

    def asphalt_weight(self, weight_of_square_meter, thickness):
        self.weight_of_square_meter = weight_of_square_meter
        self.road_thickness = thickness
        return Road.square(self) * self.weight_of_square_meter * self.road_thickness / 1000


road_length = int(input('Введите длину дороги в метрах: '))
road_width = int(input('Введите ширину дороги в метрах: '))

road_1 = Road(road_length, road_width)
print(f'Площадь дорожного полотна: {road_1.square()} квадратных метров.')

print('Для расчета массы асфальта, необходимого для покрытия всего дорожного полотна введите:')
road_thickness = int(input('толщину дорожного полотна в сантиметрах: '))
asphalt_consumption = int(input('расход асфальта на м2 при толщине слоя 1 см: '))
asphalt_mass = road_1.asphalt_weight(asphalt_consumption, road_thickness)
print(f'Требуемая масса асфальта: {asphalt_mass} тонн')
