amount, str_number = 0, input()
with open('task5.txt', 'w') as new_file:
    try:
        numbers = str_number.split(' ')
        new_file.write(str_number)
        for i in numbers:
            amount += float(i)
        print('{:.2f}'.format(amount))
    except:
        print('Некорректный ввод')
