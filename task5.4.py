try:
    my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    with open('new.txt', 'r') as my_file:
        with open('new_new.txt', 'w') as new_my_file:
            for line in my_file:
                new_my_file.write(my_dict.get(line.split(' — ')[0]) + ' — ' + line.split(' — ')[1])
except:
    print('Некорректный файл')