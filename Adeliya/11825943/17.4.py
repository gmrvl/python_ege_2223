file = open('17.4.txt')
count = 0
maxsumm = 0

lastlast = int(file.readline())
last = int(file.readline())

for i in file:
    i = int(i)
    a = sorted([lastlast, last, i])
    if a[2]**2 == (a[0]**2 + a[1]**2):
        count += 1
    lastlast = last
    last = i