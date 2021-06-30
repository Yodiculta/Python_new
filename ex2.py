# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
import copy


def inputting(a):
    i = input('input elem: ')
    while i:
        a.append(i)
        inputting(a)
        return a


def swapping(lis1):
    for i in range(len(lis1)):
        if i % 2 == 0:
            b = copy.copy(lis1[i])
        else:
            lis1[i - 1] = copy.copy(lis1[i])
            lis1[i] = copy.copy(b)


list1 = inputting(list())
print(list1)
swapping(list1)
print(list1)
