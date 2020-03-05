input_number = int(input("Введите число="))

if input_number <10:
    input_number = input_number + input_number * 10 + input_number + input_number * 100 + input_number * 10 + input_number
    print(input_number)
else:
    print('Нео3бходимо вести число меньше 10')