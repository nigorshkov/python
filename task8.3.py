class Exept(Exception):
    def __init__(self, txt):
        self.txt = txt


list_value = []
while True:
    input_str = input()
    if input_str == 'stop':
        print(list_value)
        break
    try:
        if input_str.isdigit():
            list_value.append(input_str)
        else:
            raise Exept('Не число')
    except Exept as error:
        print(error)
