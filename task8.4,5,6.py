from abc import ABC, abstractmethod


class Warehouse:
    dict_printer = {}
    dict_scanner = {}
    dict_copier = {}

    @abstractmethod
    def send_warehouse(self):
        pass


class Office_equipment:
    count = 0

    def __init__(self, manufacturer, model, price):
        self.manufacturer = manufacturer
        self.model = model
        self.price = price
        Office_equipment.count += 1


class Printer(Office_equipment):
    def __init__(self, manufacturer, model, price, printing_technology, print_color):
        super().__init__(manufacturer, model, price)
        self.printing_technology = printing_technology
        self.print_color = print_color

    @property
    def send_warehouse(self):
        if Warehouse.dict_printer.get(self.model) is not None:
            Warehouse.dict_printer[self.model] = Warehouse.dict_printer[self.model] + 1
        else:
            Warehouse.dict_printer[self.model] = 1

    def __str__(self):
        return f'{self.manufacturer}, {self.model}, {self.price}, {self.printing_technology}, {self.print_color}'


class Scanner(Office_equipment):
    def __init__(self, manufacturer, model, price, type):
        super().__init__(manufacturer, model, price)
        self.type = type
        Warehouse.list_scanner.append(self)

    def __str__(self):
        return f'{self.manufacturer}, {self.model}, {self.price}, {self.type}'

    @property
    def send_warehouse(self):
        if Warehouse.dict_scanner.get(self.model) is not None:
            Warehouse.dict_scanner[self.model] = Warehouse.dict_scanner[self.model] + 1
        else:
            Warehouse.dict_scanner[self.model] = 1


class Copier(Office_equipment):
    def __init__(self, manufacturer, model, price, speed):
        super().__init__(manufacturer, model, price)
        self.speed = speed
        Warehouse.list_copier.append(self)

    def __str__(self):
        return f'{self.manufacturer}, {self.model}, {self.price}, {self.speed}'

    @property
    def send_warehouse(self):
        if Warehouse.dict_copier.get(self.model) is not None:
            Warehouse.dict_copier[self.model] = Warehouse.dict_copier[self.model] + 1
        else:
            Warehouse.dict_copier[self.model] = 1


def add():
    name_equi = input('Что вы хотите добавить?\n'
                      'Нажмите p, если Принтер\n'
                      'Нажмите s, если Сканер\n'
                      'Нажмите с, если Ксерокс\n')
    if name_equi == 'p':
        new_object = Printer(input('manufacturer: '), input('model: '), input('price: '),
                             input('printing_technology: '), input('print_color: '))
        new_object.send_warehouse
    elif name_equi == 's':
        new_object = Scanner(input('manufacturer: '), input('model: '), input('price: '), input('type: '))
        new_object.send_warehouse
    elif name_equi == 'c':
        new_object = Copier(input('manufacturer: '), input('model: '), input('price: '), input('speed: '))
        new_object.send_warehouse
    else:
        print('Команда не определенна')


def show():
    command_show = input('Колличесво какого товара вы хотите посмотреть на складе?\n'
                         'Нажмите p, если Принтер\n'
                         'Нажмите s, если Сканер\n'
                         'Нажмите с, если Ксерокс\n')
    if command_show == 'p':
        for i in Warehouse.dict_printer:
            print(f'Модель={i} : Количество={Warehouse.dict_printer[i]}')
    elif command_show == 's':
        for i in Warehouse.dict_scanner:
            print(f'Модель={i} : Количество={Warehouse.dict_scanner[i]}')
    elif command_show == 'c':
        for i in Warehouse.dict_copier:
            print(f'Модель={i} : Количество={Warehouse.dict_copier[i]}')
    else:
        print('Команда не определенна')


while True:
    name_command = input('Что вы хотите сделать?\n'
                         'Для добавления напишите add\n'
                         'Для просмотра колличесвта товара напишите show\n'
                         'Для окончания напишите exit\n')
    if name_command == 'add':
        add()
    elif name_command == 'show':
        show()
    elif name_command == 'exit':
        break
    else:
        print('Команда не определенна')
