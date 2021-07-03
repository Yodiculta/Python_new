# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. +
# При нажатии Enter должна выводиться сумма чисел. +
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. +
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. +
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def summorize(str, sum):
    arr = str.split(' ')
    for i in arr:
        if i == '*':
            return sum, 1
        if i.isdigit():
            sum += int(i)
    return sum, 0


def hello_func():
    print('you are welcome to input numbers divided by space or * to exit')
    str = input('input string of numbers divided by space: ')
    return str


def main():
    str = ''
    sum = 0
    flag = 0
    while str != '*' and flag != 1:
        str = hello_func()
        sum, flag = summorize(str, sum)
        print(f'the sum of numbers:{sum}')

main()