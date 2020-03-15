import random
from functools import reduce


def my_func(arg1, arg2):
    return arg1 * arg2


my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(my_list)
print(reduce(my_func, my_list))
