from sys import argv


def my_func(worked_hour, rate, benefit):
    try:
        worked_hour = float(worked_hour)
        rate = float(rate)
        benefit = float(benefit)
        return worked_hour * rate + benefit
    except:
        print('Not correct data')
    return 0


print(my_func(argv[1], argv[2], argv[3]))
