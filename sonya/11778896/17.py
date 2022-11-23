file = open('17.txt')

last = 0
maxsumm = 0
k = 0

for n in file:
    summ = last + int(n)
    if int(n) % 5 == 0 and summ % 7 == 0:
        k += 1
        if maxsumm < summ:
            maxsumm = summ
    last = int(n)
if maxsumm < summ:
    maxsumm = summ
print(k,maxsumm)