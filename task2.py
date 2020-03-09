input_time = int(input("Введите время в секундах="))
hours: int = input_time // 3600
minutes = (input_time // 60) % 60
seconds = input_time % 60

print(f'{hours:>02}:{minutes:>02}:{seconds:>02}')
