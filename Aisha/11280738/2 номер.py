for i in range(1,10001):
    x = i
    a = 0
    b = 0
    while x > 0:
        a += 1
        b += x % 10
        x //= 10
    if a == 2 and b == 11:
        print(i)
