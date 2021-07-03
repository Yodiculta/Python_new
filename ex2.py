# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def input_param():
    name = input('input name: ')
    s_name = input('input second name: ')
    city = input('input city: ')
    email = input('input email: ')
    phone = input('input phone: ')
    return [name, s_name, city, email, phone]


def output_param(name, s_name, city, email, phone):
    print(f"name is {name}, second name is {s_name}, live in {city}, email:{email}, phone:{phone}")


data=input_param()
output_param(name=data[0], s_name=data[1],
             city=data[2], email=data[3], phone=data[4]
             )