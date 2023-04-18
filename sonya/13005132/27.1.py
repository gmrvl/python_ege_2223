#Дана последовательность целых чисел. Необходимо найти
# максимально возможную сумму её непрерывной подпоследовательности,
# в которой количество положительных нечётных
# элементов кратно k=30
file = open('27.1-B.txt')
N = int(file.readline())
ostatki = [0 for i in range(30)]
summ = 0
nechet = 0
maxsumm = 0
for n in file:
    n = int(n)
    summ += n
    if (n % 2 == 1) and (n > 0):
        nechet += 1
    if ostatki[nechet % 30] > summ:
            ostatki[nechet % 30] = summ
    maxsumm = max(maxsumm, summ - ostatki[nechet % 30])
print(maxsumm)

