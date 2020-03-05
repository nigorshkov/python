a = float(input("Введите значение a="))
b = float(input("Введите значение b="))
count_day = 1
while a < b:
    a *= 1.1
    count_day += 1
else:
    print('Ответ: на {}-й день спортсмен достиг результата — не менее {} км.'.format(count_day, b))
