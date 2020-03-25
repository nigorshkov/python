from abc import ABC, abstractmethod


class Clothes:
    all_sum = 0
    def __init__(self, size, height):
        self.size = size
        self.height = height
        if size != 0:
            Clothes.all_sum += size/6.5 + 0.5
        elif height != 0:
            Clothes.all_sum += 2 * height + 0.3

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.size = size

    @property
    def consumption(self):
        return self.size/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.height = height

    @property
    def consumption(self):
        return 2 * self.height + 0.3


a = Coat(13, 0)
b = Suit(0, 2)
print(f'Расхода ткани для пальто= {a.consumption}')
print(f'Расхода ткани для костюма= {b.consumption}')
print(f'Общий подсчет расхода ткани= {b.all_sum}')
