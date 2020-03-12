def my_func(arg_1, arg_2):
    try:
        arg_1 = int(arg_1)
        arg_2 = int(arg_2)
    except ValueError:
        return print('Введены не цифры')
    return arg_1 ** arg_2


print(my_func(input('Введите первое число='), input('Введите второе число=')))
