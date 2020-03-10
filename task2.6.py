goods = []
list_name = []
list_price = []
list_count = []
list_unit = []
char = {}

flag = 1
i = 1
while flag:
    if input('Для добавления записи нажмите "+" ') == '+':
        list_name.append(input('название: '))
        list_price.append(input('цена: '))
        list_count.append(input('количество: '))
        list_unit.append(input('eд: '))
        char = {'название': list_name[-1], 'цена': list_price[-1], 'количество': list_count[-1], 'eд': list_unit[-1]}
        goods.append((i, char))
        i += 1
    else:
        flag = 0
# Оставляем уникальные значения
list_name = list(set([name for name in list_name]))
list_price = list(set([price for price in list_price]))
list_count = list(set([count for count in list_count]))
list_unit = list(set([unit for unit in list_unit]))
analytics = {'название': list_name, 'цена': list_price, 'количество': list_count, 'ед': list_unit}
print(goods)
print(analytics)
