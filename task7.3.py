class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        return Cell(self.count - other.count)

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def make_order(self, count_cells):
        str = ''
        if self.count > 0:
            elem = range(int(self.count / count_cells))
            for i in elem:
                str += f'{"*" * count_cells}\\n'
            str += f'{"*" * (self.count % count_cells)}'
            return print(str)
        else:
            print('<0')


a = Cell(5)
b = Cell(2)
c1 = a + b
c2 = a - b
c3 = a * b
c4 = a / b
a.make_order(2)
c1.make_order(2)
c2.make_order(2)
c3.make_order(2)
c4.make_order(2)
