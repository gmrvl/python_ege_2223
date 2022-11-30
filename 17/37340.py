# В файле содержится последовательность из 10000 целых положительных чисел.
# Каждое число не превышает 10000. Определите и запишите в ответе
# сначала количество пар элементов последовательности,
# разность которых четна и хотя бы одно из чисел делится на 31,
# затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два различных элемента последовательности.
# Порядок элементов в паре не важен.

file = open("37340.txt")

count = 0  # количество подходящих пар

chet = 0  # количество встретившихся четных чисел
max_chet = 0
nechet = 0  # количество нечетных
max_nechet = 0
chet31 = 0  # кол-во чет, которые делятся на 31
max_chet31 = 0
max2_chet31 = 0
nechet31 = 0  # кол-во нечет, которые делятся на 31
max_nechet31 = 0
max2_nechet31 = 0

for digit in file:
    digit = int(digit)
    if digit % 2 == 0 and digit % 31 == 0:
        count += chet
        chet += 1
        chet31 += 1

        if digit > max_chet31:
            max2_chet31 = max_chet31
            max_chet31 = digit
        elif digit > max2_chet31:
            max2_chet31 = digit
    elif digit % 2 != 0 and digit % 31 == 0:
        count += nechet
        nechet += 1
        nechet31 += 1

        if digit > max_nechet31:
            max2_nechet31 = max_nechet31
            max_nechet31 = digit
        elif digit > max2_nechet31:
            max2_nechet31 = digit
    elif digit % 2 == 0 and digit % 31 != 0:
        count += chet31
        chet += 1

        if digit > max_chet:
            max_chet = digit
    elif digit % 2 != 0 and digit % 31 != 0:
        count += nechet31
        nechet += 1

        if digit > max_nechet:
            max_nechet = digit
max_sum = max(max_chet + max_chet31, max_nechet + max_nechet31, max_chet31 + max2_chet31, max_nechet31 + max2_nechet31)

print(count, max_sum)
