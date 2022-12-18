count = 0
for n in range(1000, 10000):
    n = str(n)
    if int(n[0]) % 2 == 0:
        r = int(n[0]) + int(n[2]) + abs(int(n[1]) - int(n[3]))
    else:
        a = [n[0], n[1], n[2], n[3]]
        a.sort()
        r = int(a[0] + a[1] + a[2] + a[3])
        r = bin(r)[2:]
        r = int(r.count('1'))
    if r > 20:
        count += 1
print(count)