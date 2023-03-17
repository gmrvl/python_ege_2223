
for i in range(103, 100000):
    if i % 103 == 0:
        n = str(i)
        n = list(n)
        if n == sorted(n):
            print(i, i // 103)