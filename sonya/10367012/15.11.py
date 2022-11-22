def dell(n, m):
    if n % m == 0:
        return True
    else:
        return False

def f(x, A):
    return ((A < 50) and (not(dell(x, A))) <= (dell(x, 10) <= (not(dell(x, 18)))))

for A in range(1, 1000):
    ok = True
    for x in range(1, 1000):
        if f(x, A) != 1:
            ok = False
            break
    if ok:
        print(A)