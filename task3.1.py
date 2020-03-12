def division(arg_1, arg_2):
    try:
        arg_1 = float(arg_1)
        arg_2 = float(arg_2)
    except ValueError:
        return print('Введены не цифры')
    try:
        return arg_1 / arg_2
    except ZeroDivisionError:
        return print('Деление на 0')


number1 = input('Введите первое число=')
number2 = input('Введите второе число=')
print(division(number1, number2))
