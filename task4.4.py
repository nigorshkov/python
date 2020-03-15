import random


my_list = [random.randint(0,5) for i in range(10)]
print(my_list)
print([i for i in my_list if my_list.count(i) == 1])
