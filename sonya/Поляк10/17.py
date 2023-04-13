file = open('17-328.txt')
s = 0
i = 0

for n in file:
    n = int(n)
    if n % 2 == 1:
        s += n
        i += 1
srarifm = s // i

file = open('17-328.txt')
count = 0
maxsumm = 0
plast = int(file.readline())
last = int(file.readline())
for n in file:
    n = int(n)
    if (oct(n + last)[2:]).count('7') == 0 and (oct(n + plast)[2:]).count('7') == 0 and (oct(plast + last)[2:]).count('7') == 0:
        summ = n + last + plast
        if summ < srarifm:
            count += 1
            maxsumm = max(maxsumm, summ)
    plast = last
    last = n
print(count, maxsumm)
