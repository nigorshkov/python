from itertools import cycle
import random


def repeat_list():
    my_list = [random.randint(0, 100) for i in range(5)]
    for i in cycle(my_list):
        print(i)
