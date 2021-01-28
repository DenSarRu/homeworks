# Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать
# любую подходящую структуру, например словарь.
class WarehouseError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AddWarehouseError(WarehouseError):
    def __init__(self, text):
        self.text = f"Невозможно добавить товар на склад:\n {text}"


class TransferWarehouseError(WarehouseError):
    def __init__(self, text):
        self.text = f"Ошибка прередачи оборудования:\n{text}"


class Warehouse:
    def __init__(self):
        self.department = []
        self._warehouse = {}

    def add(self, elem: 'OfficeEquipment', count):
        if not isinstance(elem, OfficeEquipment):
            raise AddWarehouseError(f"{elem} не оргтехника")
        else:
            elem = str(elem)
            if elem in self._warehouse.keys():
                self._warehouse[elem]['общее количество'] += count
            else:
                self._warehouse[elem] = {
                    "общее количество": count
                }

    def transfer(self, elem: 'OfficeEquipment', count, dep):
        elem = str(elem)
        try:
            if self._warehouse[elem]['общее количество'] < count:
                raise TransferWarehouseError(f'На складе нет такого количества "{elem}". Спросите в других отделах.')
            self._warehouse[elem]['общее количество'] -= count
            self._warehouse[elem][dep] = count
            self.department.append(dep)
            print(f'Оборудование: {elem} в кол-ве {count} шт. перемещено в {dep}')
        except TransferWarehouseError as err:
            print(err)

    def __str__(self):
        print_list = [[k, v] for k, v in self._warehouse.items()]
        print_list = '\n'.join(map(str, [f'{i}\n\t{j}' for i, j in print_list]))
        return f'Список устройств на складе:\n{print_list}'


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


storage_1 = Warehouse()
storage_1.add(Printer("Samsung", "Xpress SL-M2820"), 8)
storage_1.add(Printer("Samsung", "Xpress SL-M2820"), 2)
storage_1.add(Scanner("CANON", "FC-108"), 4)
storage_1.add(Printer("HP", "LaserJet 1120"), 10)
storage_1.add(Printer("Samsung", "Xpress SL-M2820"), 89)
printer_1 = Printer("HP", "LaserJet 1320")
storage_1.add(printer_1, 5)
print(storage_1)
print()
storage_1.transfer(printer_1, 5, 'Отдел кадров')
print()
print(storage_1)
storage_1.transfer(printer_1, 5, 'Бухгалтерия')
