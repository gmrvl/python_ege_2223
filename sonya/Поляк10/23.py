def f(x,y,n,m):
    if x > y:
        return 0
    if x == y:
        if n > m:
            return 1
        else:
            return 0
    else:
        return f(x + 1, y, n, m + 1) + f(x * 2, y, n + 1, m) + f(x * 5, y, n + 1,m)
print(f(3,260,0,0))