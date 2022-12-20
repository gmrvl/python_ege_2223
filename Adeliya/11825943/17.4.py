file = open('17.4.txt')
count = 0
maxsumm = 0
summ=0
lastlast = int(file.readline())
last = int(file.readline())

for i in file:
    i = int(i)
    a = sorted([lastlast, last, i])
    if a[2]**2 == (a[0]**2 + a[1]**2):
        count += 1
        summ= i + last + lastlast
        if summ > maxsumm:
            maxsumm=summ
    lastlast = last
    last = i
if summ >maxsumm:
    maxsumm=summ
print(count,maxsumm)