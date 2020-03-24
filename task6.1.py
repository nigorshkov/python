import time

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        for i in range(3):
            print('{}'.format(self.__color[i]))
            if i == 0:
                time.sleep(7)
            elif i == 1:
                time.sleep(2)
            elif i == 2:
                time.sleep(7)

a = TrafficLight()
a.running()
