for i in range(1, 1000):
    s = i
    n = 1
    while s < 47:
        s += 4  # s = s + 4
        n *= 2
    if n == 64:
        print(i)
        break
