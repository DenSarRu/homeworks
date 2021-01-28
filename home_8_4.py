# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Warehouse:
    def __init__(self, name, location, person):
        self.warehouse_name = name
        self.warehouse_location = location
        self.responsible_person = person


class OfficeEquipment:
    def __init__(self, a_type: str, vendor: str, model: str):
        self.type = a_type
        self.vendor = vendor
        self.model = model

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model}"


class Printer(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('Принтер', *args)


class Scanner(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('Сканер', *args)