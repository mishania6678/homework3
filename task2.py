def person_data(name, surname, birth_year, city, email, phone_number):
    return f'Имя: {name}\nФамилия: {surname}\nГод рождения: {birth_year}\nГород проживания {city}' \
           f'\nE-mail: {email}\nНомер телефона: {phone_number}'


print(person_data(name=input('Введите свое имя:'),
                  surname=input('Введите свою фамилию:'),
                  birth_year=int(input('Введите свой год рождения:')),
                  city=input('Введите свой город прроживания:'),
                  email=input('Введите свой e-mail:'),
                  phone_number=input('Введите свой номер телефона:')))

# test1