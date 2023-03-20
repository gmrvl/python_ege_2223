for i in range (1, 10001):
    x = i
    a = 1
    while x > 0:
        a *= x % 7
        x = x // 7
    if a == 40:
        print(i)
        break