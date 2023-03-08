file = open('17-336.txt')
M = 100000
for n in file:
    n = int(n)
    if n % 8 == 0 and n != 8:
        M = min(M,n)


file = open('17-336.txt')
count = 0
last = int(file.readline())
minsumm = 1000000000
ns = 0
for n in file:
    n = int(n)
    if n % M == 0 and last % M == 0:
        count += 1
        summ = last + n
        if minsumm > summ:
            minsumm = summ
            ns = max(n, last)
    last = n
print(count, ns)
