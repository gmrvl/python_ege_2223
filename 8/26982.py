count = 0
for i in range(100000, 1000000):
    if i % 5 == 0:
        a = list(map(int, str(i)))
        b = sorted(a)
        if b[0] != b[1] and b[1] != b[2] and b[2] != b[3] and b[3] != b[4] and b[4] != b[5]:
            print(i)
            if a[0] % 2 == 0 and a[2] % 2 == 0 and a[4] % 2 == 0 and a[1] % 2 == 1 and a[3] % 2 == 1 and a[5] % 2 == 1:
                count += 1
            elif a[1] % 2 == 0 and a[3] % 2 == 0 and a[5] % 2 == 0 and a[0] % 2 == 1 and a[2] % 2 == 1 and a[4] % 2 == 1:
                count += 1

print(count)