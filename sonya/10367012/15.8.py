def F(x, y, A):
    return (y + 2*x != 48) or (A < x) or (A < y)

for A in range(1000):
    OK = True
    for x in range(1000):
        for y in range(1000):
            if F(x, y, A) != 1:
                OK = False
                break
    if OK:
        print(A)