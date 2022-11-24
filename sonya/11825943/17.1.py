file = open('17.1.txt')

counts = 0
maxsumm = 0
last = 2
summ = 0

for n in file:
     n = int(n)
     if last % 3 == 0 or n % 3 == 0:
         counts += 1
         summ = last + n
         if maxsumm < summ:
             maxsumm = summ
     last = n
if maxsumm < summ:
    maxsumm = summ
print(counts, maxsumm)