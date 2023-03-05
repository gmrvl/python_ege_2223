file = open('inf_22_10_20_27b.txt')
n = int(file.readline())
minsumm = 0
maxx = 0
for i in file:
    a, b = i.split(' ')
    a = int(a)
    b = int(b)
    minsumm += min(a,b)
    maxx = max(maxx, max(a,b))
if minsumm % 3 != 0:
    print(minsumm - maxx)
else:
    print(minsumm)
