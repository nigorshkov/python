class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return '{} {}'.format(self.surname, self.name)

    def get_total_income(self):
        return '{} {}'.format(self._income['wage'], self._income['bonus'])

a = Position('Петр', 'Петров', 'продавец', '15000', '5000')
print(a.get_full_name())
print(a.get_total_income())