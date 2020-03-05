input_time = int(input("Введите время в секундах="))
hours: int = input_time // 3600
minutes = (input_time // 60) % 60
seconds = input_time % 60

if hours < 10:
    hours = str('0' + str(hours))
if minutes < 10:
    minutes = str('0' + str(minutes))
if seconds < 10:
    seconds = str('0' + str(seconds))

print(hours, ":", minutes, ":", seconds)
