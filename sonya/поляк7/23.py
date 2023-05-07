def f(x,y,n = 0):
    if x == y:
        return 1
    if x > y or (n > 3):
        return 0
    return f(x + 2,y,n) + f(x * 3, y,  n + 1) + f(x * 5, y, n + 1)
print(f(2,200))

