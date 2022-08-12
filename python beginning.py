
for i in range(0, 100):
    s = i
    for j in range(0, 100):
        x = j
        s = 100*s + x
        n = 1
        while s < 2021:
            s = s + 5*n
            n = n + 1
        if n == 15:
            print(i, j)
            break


