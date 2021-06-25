# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
d = input()

# max = 0
# for i in d:
#     if int(i) > max:
#         max = int(i)
# print(max)

maxi=0
def maxCount(num, maxi, t_len):
    t_len -= 1
    while int(t_len) >= 0:
        next = num % 10
        if next > maxi:
            maxCount(num // 10, next, t_len)
        elif maxi >= next:
            maxCount(num // 10, maxi, t_len)
        return 1
    print(maxi)

    
maxCount(int(d), maxi, int(len(d)))
