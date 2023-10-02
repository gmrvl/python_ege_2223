file = open('175.txt')
min7 = 10000
for n in file:
    n = int(n)
    if abs(n) % 10 == 7:
        min7 = min(min7, n)

file = open('175.txt')
count = 0
maxsumm = 0
last = int(file.readline())
for n in file:
    n = int(n)
    if (abs(n) % 10== 7 and abs(last) % 10 != 7) or (abs(n) % 10 != 7 and abs(last) % 10 == 7):
        if (n**2 + last**2) < min7**2:
            count += 1
            maxsumm = max(maxsumm, n**2 + last**2)
    last = n
print(count, maxsumm)
