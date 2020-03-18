try:
    with open('staff.txt', 'r') as staff:
        amount,count = 0, 0
        for line in staff:
            if int(line.split(' ')[1][0:-1]) >= 20000:
                print(line.split(' ')[0])
            amount += int(line.split(' ')[1][0:-1])
            count += 1
        print('Средней величины дохода сотрудников ={:.2f}'.format(amount / count))
except:
    print('Некорректный файл')
