for i in range(1, 10001):
    x = i
    a = 0
    b = 1
    while x > 0:
        a += 1
        b *= x % 10
        x = x // 10
    if a == 3 and b == 7:
        print(i)
