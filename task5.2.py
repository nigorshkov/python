count_str = 0
with open('new.txt', 'r') as new_file:
    for line in new_file:
        print(line[0:-1], ", количества слов = ", len(line.split(' ')))
        count_str += 1
    print('Количество строк =', count_str)
