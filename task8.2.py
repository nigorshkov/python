class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    inp_arg1 = int(input("Введите 1 число: "))
    inp_arg2 = int(input("Введите 2 число: "))
    if inp_arg2 == 0:
        raise OwnError("Делить на 0 нельзя")
except ValueError:
    print("Вы ввели не числа")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Деление= {inp_arg1/inp_arg2}")