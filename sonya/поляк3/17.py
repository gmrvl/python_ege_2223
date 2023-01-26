#Найдите такие пары элементов, в которых произведение элементов больше, чем произведение рядом стоящих чисел (перед и после пары).
# В качестве ответа выведите максимальную сумму среди найденных пар,
# затем количество таких из этих пар, в которых есть хотя бы одно число, большее среднего арифметического всех чисел в файле.
file = open('17-341.txt')
s = 0
i = 0
for nn in file:
    nn = int(nn)
    s += nn
    i += 1

ssrarifm = s // i
print(ssrarifm)
file = open('17-341.txt')

count = 0
maxsumm = 0
pplast = int(file.readline())
plast = int(file.readline())
last = int(file.readline())

for n in file:
    n = int(n)
    if last * plast > n * pplast:
        maxsumm = max(maxsumm, plast + last)
        if plast > ssrarifm or last > ssrarifm:
            count += 1
    pplast = plast
    plast = last
    last = n
print(maxsumm,count)