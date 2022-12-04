#задание5
count = 0
for i in range(1000, 10000):
    n = str(i)
    s = n[0]
    r8 = ''
    if int(s) % 4 == 0:
        if s == '4':
            r = n.replace('4', '9', 1)
        if s == '8':
            r = n.replace('8', '9', 1)
        r = int(r)
        while r > 0:
            r8 = str(r % 8) + r8
            r //= 8
        if r8[-1] == '4':
            count += 1
    if int(s) % 2 == 0 and int(s) % 4 != 0:
        if s == '2':
            r = n.replace('2', '3', 1)
        if s == '6':
            r = n.replace('6', '3', 1)
print(count)

