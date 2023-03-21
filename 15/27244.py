def F(x, y, A):
    return (x * y < 121) or (y > A) or (x >= A)


for A in range(1000):
    s = True
    for x in range(1000):
        for y in range(1000):
            if F(x, y, A) == 0:
                s = False
                break
        # if not s:
        #     break
    if s:
        print(A)