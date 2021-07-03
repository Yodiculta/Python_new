# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func1(x:int, y:int):
    return x**y

def main():
    try:
        X = float(input('input X: '))
        Y = int(input('input Y: '))
        if X > 0 and Y < 0 and  Y % 1 ==0:
            print(my_func1(X, Y))
        else:
            print('Введите действительное положительное число x и целое отрицательное число y')
    except ValueError:
        return
main()