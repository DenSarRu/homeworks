from abc import ABC, abstractmethod


class Clothes(ABC):
    """
    Класс для расчета суммарного расхода ткани на производство одежды
    """
    def __init__(self, v, h):
        self.size = v
        self.growth = h

    @abstractmethod
    def fabric_consumption(self):
        pass

    @property
    def full_square(self):
        return f'Общий расход ткани: {round((self.size / 6.5 + 0.5) + (2 * self.growth + 0.3))} м.кв.'


class Coat(Clothes):

    @property
    def fabric_consumption(self):
        return 'Расход ткани на одно пальто размера {}: {:.3f} м.кв.'.format(self.size, self.size / 6.5 + 0.5)


class Costume(Clothes):

    @property
    def fabric_consumption(self):
        return 'Расход ткани на один костюм роста {}: {:.2f} м.кв.'.format(self.growth, 2 * self.growth + 0.3)


print('Для определения расхода ткани по каждому типу одежды введите:')
size = float(input('Размер (для пальто): '))
growth = float(input('Рост (для костюма): '))
coat_1 = Coat(size, growth)
costume_1 = Costume(size, growth)
print(coat_1.fabric_consumption)
print(costume_1.fabric_consumption)
print(coat_1.full_square)
