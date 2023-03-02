def f(n,m,A):
    return (3*m + 4*n > 63) or ((m <= A) and (n < A))

for A in range(0,100):
    ok = True
    for m in range(0,100):
        for n in range(0,100):
            if f(n,m,A) != 1:
                ok = False
    if ok:
        print(A)