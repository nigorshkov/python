list_str = input('Введите строку: ').split(' ')
for ind, i in enumerate(list_str):
    if len(i) > 10:
        print(f"{ind+1} {i [0:10]}")
    else:
        print(ind+1, i)
