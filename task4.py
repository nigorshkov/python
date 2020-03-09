while True:
    input_number = input("Введите число=")
    if input_number.isdigit():
        input_number = int(input_number)
        break
    else:
        print('Вы ввели не число')
max = 0
while input_number > 0:
    if (input_number % 10) > max:
        max = input_number % 10
    input_number = input_number // 10
print(max)