file = open('17-338.txt')
minn = 100000
for n in file:
    n = int(n)
    minn = min(minn, n)

file = open('17-338.txt')
last = int(file.readline())
maxsumm = 0
count = 0
for n in file:
    n = int(n)
    if (n % 117 == minn) or (last % 117 == minn):
        count += 1
        maxsumm = max(maxsumm, n + last)
    last = n
print(count, maxsumm)