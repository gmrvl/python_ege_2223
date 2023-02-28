file = open('27-B_1.txt')
n = int(file.readline())
maxsumm = 0
minn = 1000000
for i in file:
    a, b = i.split(' ')
    a = int(a)
    b = int(b)
    maxsumm += max(a,b)
    minn = min(minn, min(a,b))
if maxsumm % 5 == 0:
    print(maxsumm - minn)
else:
    print(maxsumm)
