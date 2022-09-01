for i in range(1, 10001):
    a = 10
    b = 0
    x = i
    while x > 0:
        y = x % 10
        x = x // 10
        if y < a:
            a = y
        if y > b:
            b = y
    if a == 5 and b == 7:
        print(i)
