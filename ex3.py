# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

dictionary = {
    'winter': [1, 2, 12],
    'spring': [4, 5, 3],
    'summer': [7, 8, 6],
    'autumn': [10, 11, 9]
}
i = input('input the number of month: ')
for el in dictionary:
    if int(i) in dictionary[el]:
        print(f"The month is: {el}")
