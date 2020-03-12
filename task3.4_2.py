def my_func(arg_1, arg_2):
    step = 1
    try:
        arg_1 = float(arg_1)
        arg_2 = int(arg_2) * (-1)
    except ValueError:
        return print('Введены не цифры')
    for i in range(1, arg_2 + 1):
        step *= float(1 / arg_1)
    return step


print(my_func(input('Введите первое число='), input('Введите второе число=')))
