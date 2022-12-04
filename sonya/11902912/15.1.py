def F(x,y,A):
    return (x * y < 140) or (y > A) or (x > A)

for A in range(100):
    ok = True
    for x in range(100):
        for y in range(100):
            if F(x,y,A) != 1:
                ok = False
                break
    if ok:
        print(A)
