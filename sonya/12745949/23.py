def f(x,y, Flag):
    if x == y:
        return 1
    if x > y:
        return 0
    if Flag:
        return f(x + 1, y, True) + f(x + 2, y, True) + f(x * 2, y, False)
    else:
        return f(x + 1, y, True) + f(x + 2, y, True)
print(f(1,11, True))