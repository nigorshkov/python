import random


my_list = [random.randint(0,100) for i in range(10)]
change_list = [i for i in my_list if i > my_list[my_list.index(i)-1]]
print(my_list)
print(change_list)