# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().
import re


def int_func(str):
    new_str=''
    for each in str.split():
        if re.search(r'[^a-zA-Z]', each):
            print("not latin")
        else:
            each.title()
            print(each)
            new_str.join(each)
            print(new_str)
            print(each)
    print(new_str)
    return str


def main():
    str = input('input word:\n')
    str = int_func(str)
    print(str)


main()