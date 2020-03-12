def info(name, surname, year, city, email, phone):
    print(
        f"имя - {name}, фамилия - {surname}, год  рождения  - {year}, город проживания - {city}, email - {email}, "
        f"телефон - {phone}")


info(name=input('Введите имя: '), surname=input('Введите фамилия: '), year=input('Введите год  рождения: '),
     city=input('Введите город проживания: '), email=input('Введите email: '), phone=input('Введите телефон: '))
