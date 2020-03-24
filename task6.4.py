class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина {} поехала'.format(self.name))

    def stop(self):
        print('Машина {} остановилась'.format(self.name))

    def turn(self, direction):
        print('Машина {} повернула {}'.format(self.name, direction))

    def show_speed(self):
        print('Скорость= {}'.format(self.speed))

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('Машина {} превысила скорость, скорость= {}'.format(self.name, self.speed))
        else:
            print('Скорость= {}'.format(self.name, self.speed))

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print('Машина {} превысила скорость, скорость= {}'.format(self.name, self.speed))
        else:
            print('Машина {}, скорость= {}'.format(self.name, self.speed))

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(70, 'Red', 'Kia', False)
sport_car = SportCar(100, 'Green', 'Porsche', False)
work_car = WorkCar(30, 'Black', 'Gazel', False)
police_car = PoliceCar(60, 'White', 'Ford', True)

town_car.go()
town_car.turn('лево')
town_car.show_speed()
print(town_car.is_police)
print()
sport_car.stop()
sport_car.turn('направо')
sport_car.show_speed()
print()
work_car.show_speed()
print()
police_car.go()
print(police_car.is_police)
