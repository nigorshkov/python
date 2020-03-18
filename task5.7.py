import json


with open('task7.txt') as my_file:
    average, count, my_dict = 0, 0, {}
    for line in my_file:
        profit = float(line.split(' ')[2]) - float(line.split(' ')[3])
        if profit > 0:
            average += profit
            count += 1
        my_dict[line.split(' ')[0]] = profit
    my_list = [my_dict, {"average_profit": average/count}]
    print(my_list)

with open('task7.json', 'w') as file_json:
    json.dump(my_list, file_json)