for i in range(1, 10001):
    a = 0
    b = 0
    x = i
    while x > 0:
        y = x % 10
        if y > 3:
            a = a+1
        if y < 8:
            b = b+1
        x = x // 10
    if a == 4 and b == 2:
        print(i)
        break
