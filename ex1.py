# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def deriv(a, b):
    if b != 0:
        return a/b
    else:
        return None


def main():
    a = input('input first number: ')
    b = input('input second number: ')
    print(deriv(float(a), float(b)))


main()

