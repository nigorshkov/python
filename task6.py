while True:
    a = input("Введите значение a=")
    if a.isdigit():
        a = int(a)
        break
    else:
        print('Вы ввели не число')

while True:
    b = input("Введите значение b=")
    if b.isdigit():
        b = int(b)
        break
    else:
        print('Вы ввели не число')

count_day = 1
while a < b:
    a *= 1.1
    count_day += 1
else:
    print('Ответ: на {}-й день спортсмен достиг результата — не менее {} км.'.format(count_day, b))
