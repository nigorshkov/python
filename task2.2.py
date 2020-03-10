list_num = []
while True:
    count = input('Введите количество элементов=')
    if count.isdigit():
        break
    else:
        print('Введите число!')

for i in range(int(count)):
    list_num.append(input('Введите {} значение списка='.format(i+1)))
print(list_num)

i = 1
while i < int(count):
    c = list_num[i]
    list_num[i] = list_num[i-1]
    list_num[i-1] = c
    i+=2
print(list_num)
