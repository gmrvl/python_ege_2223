file = open('17.txt')

counts = 0
maxsumm = 0
summ = 0
last = -1
for n in file:
    n = int(n)
    if last > -1:
        summ = last + n
        if summ % 2 == 0 or n % 19 ==0 or last % 19 == 0:
            counts += 1
            if maxsumm < summ:
                maxsumm = summ
    last = n
if maxsumm < summ:
    maxsumm = summ
print(counts,maxsumm)
