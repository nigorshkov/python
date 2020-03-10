while True:
    month = input('Введите номер месяца=')
    if month.isdigit() and 0 < int(month) < 13:
        month = int(month)
        break
    else:
        print('Неверный номер месяца!')

month_list = ['Зима', 'Весна', 'Лето', 'Осень']
month_dict = {1:'Зима', 2:'Весна', 3:'Лето', 4:'Осень'}
if month == 12 or month == 1 or month == 2:
    print(month_list[0])
    print(month_dict.get(1))
elif month ==3 or month == 4 or month == 5:
    print(month_list[1])
    print(month_dict.get(2))
elif month ==6 or month == 7 or month == 8:
    print(month_list[2])
    print(month_dict.get(3))
elif month ==9 or month == 10 or month == 11:
    print(month_list[3])
    print(month_dict.get(4))

