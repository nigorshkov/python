def func_without(str_without):
    sum_func = 0
    a = str_without.split(' ')
    for i in a:
        sum_func += int(i)
    return sum_func


def func_with(str_with):
    sum_func = 0
    a = str_with.split(' ')
    i = 0
    while a[i] != '+':
        sum_func += int(a[i])
        i += 1
    return sum_func


print('Для завершения суммирования введите "+"')
flag = 1
total = 0
while flag:
    str_num = input()
    try:
        if str_num[-1] == '+':
            total += func_with(str_num)
            flag = 0
        else:
            total += func_without(str_num)
    except ValueError:
        print('Введены некоректные значения')
    print('Сумма=', total)
