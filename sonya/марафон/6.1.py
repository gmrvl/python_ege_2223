for i in range(0,1000):
    s = i
    s = 3 * (s // 10)
    n = 1
    while s < 221:
        s = s + 13
        n = n * 2
    if n ==128:
        print(i)