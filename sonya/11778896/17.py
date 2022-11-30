file = open('17.txt')

last = int(file.readline())
maxsumm = 0
count = 0

for n in file:
    n = int(n)
    summ = last + n
    if (n % 5 == 0 or last % 5 == 0) and summ % 7 == 0:
        count += 1
        if maxsumm < summ:
            maxsumm = summ
    last = n
if maxsumm < summ:
    maxsumm = summ
print(count, maxsumm)
