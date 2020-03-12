def my_func(arg_1, arg_2, arg_3):
    try:
        arg_1 = float(arg_1)
        arg_2 = float(arg_2)
        arg_3 = float(arg_3)
    except ValueError:
        return print('Введены не цифры')
    if arg_1 < arg_2 and arg_1 < arg_3:
        return arg_2 + arg_3
    elif arg_2 < arg_1 and arg_2 < arg_3:
        return arg_1 + arg_3
    elif arg_3 < arg_1 and arg_3 < arg_2:
        return arg_1 + arg_2
    else:
        print('Имеются 2 одинаковых числа')


print(my_func(input('Ведите первое число: '), input('Ведите второе число: '), input('Ведите третье число: ')))
