file = open('17.txt')
count = 0
minsumm = 0
last = int(file.readline())
for n in file:
    n = int(n)
    if abs(n) % 10 == 4 or abs(last) % 10 == 4:
        if (n + last) % 2 == 0:
            count += 1
            minsumm = min(minsumm, n + last)
    last = n
print(count, minsumm)