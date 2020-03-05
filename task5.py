revenue = float(input("Введите значение выручки="))
cost = float(input("Введите значение издержки="))
if revenue > cost:
    print('Прибыль — выручка больше издержек')
    rent = (revenue - cost) / revenue
    print('Рентабельность=', rent)
    amount = int(input("Введите численность сотрудников="))
    print('Прибыль фирмы в расчете на одного сотрудника', rent / amount)
else:
    print('Убыток — издержки больше выручки')