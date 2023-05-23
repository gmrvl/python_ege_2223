def F(x, y, A):
    return (((x * y) < 120) or (y > A) or (x > A))

for A in range (10000):
    c = True
    for x in range (10000):
        for y in range (10000):
            if F(x,y,A) == 1:
                c = True
                break
        if c:
            break
    if c:
        print(A)

