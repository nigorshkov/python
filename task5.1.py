with open('new.txt','w') as new_file:
    while True:
        input_str = input('Введите строку:')
        if input_str != '':
            new_file.write(input_str + '\n')
        else:
            break
