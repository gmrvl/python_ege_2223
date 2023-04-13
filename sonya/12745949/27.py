#Дана последовательность натуральных чисел.
# Необходимо найти максимально возможную сумму
# её непрерывной подпоследовательности,
# в которой количество чётных элементов кратно k=10.
file = open('27-B.txt')
n = int(file.readline())
ostatki = [0 for i in range(10)]
summ = 0
maxsumm = 0
countch = 0
for n in file:
    n = int(n)
    summ += n
    if n % 2 == 0:
        countch += 1
    if countch % 10 == 0:
        maxsumm = max(maxsumm, summ)
    else:
        if ostatki[countch % 10] == 0:
            ostatki[countch % 10] = summ
        summ1 = summ - ostatki[countch % 10]
        maxsumm = max(maxsumm, summ1)
print(maxsumm)


