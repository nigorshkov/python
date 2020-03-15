def fibo_gen(numb):
    count = 1
    while count <= numb:
        yield count
        count += 1


try:
    fact_list=[]
    i=0
    fact = 1
    input_number = int(input('Введите число='))
    for el in fibo_gen(input_number):
        fact *= el
        if i < 15:
            fact_list.append(el)
        i += 1
    print(fact, '= ', fact_list)
except:
    print('Неккоректное число')