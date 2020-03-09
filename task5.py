while True:
    revenue = input("Введите значение выручки=")
    if revenue.isdigit():
        revenue = int(revenue)
        break
    else:
        print('Вы ввели не число')


while True:
    cost = input("Введите значение издержки=")
    if cost.isdigit():
        cost = int(cost)
        break
    else:
        print('Вы ввели не число')

if revenue > cost:
    print('Прибыль — выручка больше издержек')
    rent = (revenue - cost) / revenue
    print('Рентабельность=', rent)
    while True:
        amount = input("Введите численность сотрудников=")
        if amount.isdigit():
            amount = int(amount)
            break
        else:
            print('Вы ввели не число')
    print('Прибыль фирмы в расчете на одного сотрудника', rent / amount)
else:
    print('Убыток — издержки больше выручки')