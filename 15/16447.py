def F(x, y, A):
    return (2 * x + 3 * y < 30) or (x + y >= A)


for A in range(1000):
    OK = True
    for x in range(1000):
        for y in range(1000):
            if not F(x, y, A):
                OK = False
                break
        if not OK:
            break
    if OK:
        print(A)
