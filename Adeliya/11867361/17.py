# последовательность из 10000 целых положительных чисел
# сначала количество пар элементов последовательности,
#  разность которых четна и хотя бы одно из чисел делится на 19,
#  затем максимальную из сумм элементов таких пар.
#  В данной задаче под парой подразумевается два различных элемента последовательности.
#  Порядок элементов в паре не важен.
file = open('17.txt')
count = 0
ch = 0
max_ch = 0
nch = 0
max_nch = 0
ch19 = 0
maxch19 = 0
max2ch19 = 0
nch19 = 0
maxnch19 = 0
max2nch19 = 0
for i in file:
    i = int(i)
    if i % 2 == 0 and i % 19 == 0:
        count += ch
        ch += 1
        ch19 += 1
        if i > maxch19:
            max2ch19 = maxch19
            maxch19 = i
        elif i > max2ch19:
            max2ch19 = i
    if i % 2 != 0 and i % 19 == 0:
        count += nch
        nch += 1
        nch19 += 1
        if i > maxnch19:
            max2nch19 = maxnch19
            maxnch19 = i
        elif i > max2nch19:
            max2nch19 = i
    if i % 2 == 0 and i % 19 != 0:
        count += ch19
        ch += 1
        if i > max_ch:
            max_ch = i
    if i % 2 != 0 and i % 19 != 0:
        count += nch19
        nch += 1
        if i > max_nch:
            max_nch = i
maxsumm = max(max_ch + maxch19, max_nch + maxnch19, maxch19 + max2ch19, maxnch19 + max2nch19)
print(count, maxsumm)
