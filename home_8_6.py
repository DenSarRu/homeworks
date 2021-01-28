# Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
class WarehouseError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AddWarehouseError(WarehouseError):
    def __init__(self, text):
        self.text = f"Невозможно добавить товар на склад:\n{text}"


class TransferWarehouseError(WarehouseError):
    def __init__(self, text):
        self.text = f"Ошибка прередачи оборудования:\n{text}"


class ValidateError(WarehouseError):
    def __init__(self, text):
        self.text = f"Ошибка ввода:\n{text}"


class Warehouse:
    def __init__(self):
        self.department = []
        self._warehouse = {}

    @staticmethod
    def validate_input(cnt):
        """
        метод производит проверку вводимых пользователем данных
        :param cnt: передаём введённое пользователем количество оборудования
        :return: True - если введено число, иначе False
        """
        try:
            if not isinstance(cnt, int):
                return False
            return True
        except ValidateError:
            return 'Некорректный ввод'

    def add(self, elem: 'OfficeEquipment', count: int) -> None:
        """
        Метод добавления оборудования на склад
        :param elem: элемент класса OfficeEquipment - передаваемое оборудование
        :param count: количество оборудования, помещаемого на склад
        :return: None
        """
        if not isinstance(elem, OfficeEquipment):
            raise AddWarehouseError(f"{elem} не оргтехника")
        try:
            if not self.validate_input(count):
                raise AddWarehouseError(f'Внимательно проверьте вводимые данные!')
            elem = str(elem)
            if elem in self._warehouse.keys():
                self._warehouse[elem]['общее количество'] += count
            else:
                self._warehouse[elem] = {
                    "общее количество": count
                }
        except AddWarehouseError as er:
            print(er)

    def transfer(self, elem: 'OfficeEquipment', count: int, dep: str) -> None:
        """
        Метод осуществляющий перемещение оборудования между складом и отделом
        :param elem: элемент класса OfficeEquipment - передаваемое оборудование
        :param count: количество оборудования, помещаемого в отдел
        :param dep: наименование отдела
        :return: None
        """
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


storage_1.add(Printer("Xerox", "Super Device"), '4')
