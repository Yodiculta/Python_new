# 6. * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
name = list()
price = list()
count = list()
amount = list()
key = 1
tpl=tuple()


def price_input(grad):
    i = input('input price: ')
    if i.isdigit():
        grad.append(float(i))
        return 1
    else:
        return 0


def name_input(grad):
    i = input('input name: ')
    if i.isdigit() == False:
        grad.append(i)
        return 1
    else:
        return 0


def count_input(grad):
    i = input('input count: ')
    if i.isdigit():
        grad.append(float(i))
        return 1
    else:
        return 0


def amount_input(grad):
    i = input('input amount: ')
    if i.isdigit() == False:
        grad.append(i)
        return 1
    else:
        return 0


def inputting(key, name, price, count, amount):
    while key == 1:

        key = price_input(price) * name_input(name) * count_input(count) * amount_input(amount)
        inputting(key, name, price, count, amount)
    key=0
    print(name, price, count, amount)


def courtage(name, price, count, amount, tpl):
    n = name.pop()
    while n:
        tpl.append(name, price.pop(), count.pop(), amount.pop)
        print(tpl)
        courtage(name, price, count, amount, tpl)

    print(tpl)


inputting(key, name, price, count, amount)
print('hello')
courtage(name, price, count, amount, tpl)
