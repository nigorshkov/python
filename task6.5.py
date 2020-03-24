class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки, название {}. Ручка'.format(self.title))

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки, название {}. Карандаш'.format(self.title))

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки невозможен, название {}. Ручка двери'.format(self.title))

pen = Pen('parker')
pen.draw()
print()
pencil = Pencil('ozon')
pencil.draw()
print()
handle = Handle('ikea')
handle.draw()
