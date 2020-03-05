input_number = int(input("Введите число="))
max = 0
while input_number > 0:
    if (input_number % 10) > max:
        max = input_number % 10
    input_number = input_number // 10
print(max)