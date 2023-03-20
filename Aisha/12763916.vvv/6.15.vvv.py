def F(x, y, A):
    return (x and y < 121) or (y > A) or (x >= A)

for A in range (1000):
    c = True
    for x in range (1000):
        for y in range (1000):
            if F(x, y, A) == 0:
                c = False
                break
            if c:
                print(A)

