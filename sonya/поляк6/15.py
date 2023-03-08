def f(x,y,A):
    return (x + y <= 22) or (y <= x - 6) or (y >= A)

for A in range(100):
    ok = True
    for x in range(100):
        for y in range(100):
            if f(x,y,A) != 1:
                ok = False
                break
    if ok:
        print(A)
        
