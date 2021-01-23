'''
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой
'''
def user_description(name, surname, birthday='', city='', email='', phone=''):
    return f'New user: {name} {surname}, birthday:{birthday}, city:{city}, email:{email}, phone:{phone}'

name = input('input name: ')
surname = input('input surname: ')
birthday = input('input birthday: ')
city = input('input city: ')
email = input('input email: ')
phone = input('input phone: ')
print(user_description(name=name, surname = surname, birthday = birthday, email = email, city = city, phone = phone))
