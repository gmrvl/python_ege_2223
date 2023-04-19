def f(x,y,c):
    if x % 2 == 1:
        c += 1
    if x > y:
        return 0
    if x == y:
        if c <= 7:
            return 1
        else:
            return 0
    else:
        return f(x + 2,y, c) + f(x * 2, y, c) + f(x * 3, y, c)
print(f(1,214,0))