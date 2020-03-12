def int_func(arg):
    return arg.capitalize()


str_up = input('Введите строку:')
a = str_up.split(' ')
for i in a:
    print(int_func(i), end=' ')
