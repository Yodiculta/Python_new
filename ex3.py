# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


my_func=lambda A, B, C: A + B + C - min(A, B, C)


a = int(input('input a: '))
b = int(input('input b: '))
c = int(input('input c: '))
print(my_func(A=a, B=b, C=c))
