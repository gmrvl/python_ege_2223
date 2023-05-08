def l(x):
    return str(x).count('1') + str(x).count('2') * 2 + str(x).count('3') * 3 + str(x).count('4') * 4 + str(x).count('5') * 5 + str(x).count('6') * 6 + str(x).count('7') * 7 + str(x).count('8') * 8 + str(x).count('9') * 9


file = open('17-333.txt')
s = 0
i = 0
for n in file:
    n = int(n)
    if 1000 <= n < 10000:
        s += n
        i += 1
srarifm = s // i
file = open('17-333.txt')
f = [int(i) for i in file]
f = set(f)
count = 0
maxsumm = 0
file = open('17-333.txt')
last = int(file.readline())
for n in file:
    n = int(n)
    summ = n + last
    if summ not in f:
        if summ < srarifm:
            count += 1
            maxsumm = max(maxsumm, l(n) + l(last))
    last = n
print(count, maxsumm)
