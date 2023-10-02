file = open('24.17.txt').read()
maxcount = count = 0
last = 0
for n in file:
    n = int(n)
    if last > n:
        count += 1
    else:
        maxcount = max(maxcount, count)
        count = 1
    last = n
print(maxcount)