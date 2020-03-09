while True:
    input_number = input("Введите натуральное число=")
    if input_number.isdigit():
        input_number = int(input_number) + int(input_number * 2) + int(input_number * 3)
        break
    else:
        print('Вы ввели не число')
print(input_number)