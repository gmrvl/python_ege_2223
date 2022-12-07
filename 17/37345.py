# Определите и запишите в ответе сначала количество пар элементов последовательности,
# для которых произведение элементов делится без остатка на 62,
# затем максимальную из сумм элементов таких пар.
# ВНИМАТЕЛЬНО СМОТРЕТЬ МАКСИМУМЫ - МОГУТ БЫТЬ ВОПРОСЫ !!!!!!!!!!!!!!!!!!!!!!!!!!!!1

file = open('37345.txt')

count = 0

allDigit = 0
del2 = 0
del62 = 0
del31 = 0

max62 = 0
maxL = 0
max31 = 0
max2 = 0

for digit in file:
    digit = int(digit)
    if digit % 31 == 0 and digit % 2 == 0:
        count += allDigit
        del62 += 1
        del31 += 1
        del2 += 1
        if digit > max62:
            max62 = digit
    elif digit % 31 == 0 and digit % 2 != 0:
        count += del2
        del31 += 1
        if digit > max31:
            max31 = digit
    elif digit % 31 != 0 and digit % 2 != 0:
        count += del62
    elif digit % 31 != 0 and digit % 2 == 0:
        count += del31
        del2 += 1
        if digit > max2:
            max2 = digit
    allDigit += 1
    if digit > maxL and digit != max62:
        maxL = digit
maxPair = max(max2 + max31, maxL + max62)
print(count, maxPair)
