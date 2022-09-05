for i in range (1, 10001):
    x = i
    a=0; b=0
    while x > 0:
        if x%2 > 0:
            a += 1
        else:
            b += 1
        x = x//2
    if a == 3 and b == 2:
        print(i)
        break