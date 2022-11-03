def deel(x, D):
    return x % D == 0


def F(x, A):
    return (not deel(x, A)) <= (deel(x, 6) <= (not deel(x, 4)))


for A in range(1, 10000):
    c = True
    for x in range(1, 10000):
        if F(x, A) == 0:
            c = False
            break
    if c:
        print(A)
