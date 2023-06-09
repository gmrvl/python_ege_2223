def f(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

file = open('17-332.txt')
s = 0
i = 0
for n in file:
    n = int(n)
    if n % 17 == 0:
        s += n
        i += 1
sraarifm = s // i
file = open('17-332.txt')
plast = int(file.readline())
last = int(file.readline())
count = 0
sums = [0 for i in range(37)]
for n in file:
     n = int(n)
     if f(plast) == f(n) and last < sraarifm:
         count += 1
         sums[f(last)] += 1
     plast = last
     last = n
maxx = sums.index(max(sums))
print(count, maxx)