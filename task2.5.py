my_list = [7, 5, 3, 3, 2]
while True:
    element = input('Введите новый элемент рейтинга=')
    if element.isdigit():
        element = int(element)
        break
    else:
        print('Неверно указан элемент!')

for i in range(len(my_list)):
    if my_list[i] < element:
        my_list.insert(0, element)
        break
    elif my_list[i] >= element and my_list[i+1] < element:
        my_list.insert(i+1, element)
        break
    elif my_list[-1] > element:
        my_list.append(element)
        break
print(my_list)
