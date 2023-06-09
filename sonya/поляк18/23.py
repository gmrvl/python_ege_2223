def f(x,y,s,u):
    if x == y and u > s:
        return 1
    if x > y:
        return 0
    return f(x + 3, y, s + 1, u) + f(x * 2, y, s, u + 1) + f(x * 7, y, s, u + 1)
print(f(2,472,0,0))