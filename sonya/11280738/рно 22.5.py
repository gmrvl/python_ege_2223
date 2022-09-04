for i in range(1,1000001):
    x=i
    a = 0;
    b = 0
    while x > 0:
        a += 1
        if x % 2 == 0:
            b += x % 100
        x //= 10
    if a==4 and b==160:
        print(i)
