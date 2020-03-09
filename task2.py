while True:
    input_time = input("Введите время в секундах=")
    if input_time.isdigit():
        hours = int(input_time) // 3600
        minutes = int(input_time) // 60 % 60
        seconds = int(input_time) % 60
        break
    else:
        print('Вы ввели не число')
print(f'{hours:>02}:{minutes:>02}:{seconds:>02}')
