class Data:
    def __init__(self,str_date):
        self.str_date = str(str_date)

    @classmethod
    def get_value(cls, str_date):
        try:
            list_value = []
            for i in str_date.split('-'):
                list_value.append(int(i))
            return f'Day={list_value[0]}, Month={list_value[1]}, Year={list_value[2]}'
        except:
            return 'Incorect string'


    @staticmethod
    def valid(str_date):
        list_value = []
        for i in str_date.split('-'):
            list_value.append(int(i))
        if 0 < list_value[0] < 31:
            print('Correct day')
        else:
            print('Incorrect day')
        if 0 < list_value[1] < 13:
            print('Correct month')
        else:
            print('Incorrect month')
        if 0 < list_value[2]:
            print('Correct year')
        else:
            print('Incorrect year')


print(Data.get_value(input('Data: ')))
Data.valid(input('Data: '))
