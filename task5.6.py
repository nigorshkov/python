def value(type_educ):
    try:
        return type_educ[0:type_educ.index('(')]
    except:
        return 0


with open('task6.txt', 'r', encoding='utf-8') as new_file:
    my_dict = {}
    for line in new_file:
        print(line.split(' '))
        amount = int(value(line.split(' ')[1])) + int(value(line.split(' ')[2])) + int(value(line.split(' ')[3]))
        my_dict[line.split(' ')[0][0:-1]] = amount
    print(my_dict)
