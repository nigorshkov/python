from itertools import count


def gen_int_num():
    try:
        num = int(input('Введите начальное число='))
        for i in count(num):
            if i > 100:
                break
            else:
                print(i)
    except:
        print('Некорректное число')
