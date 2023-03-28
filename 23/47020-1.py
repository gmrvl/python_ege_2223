def f(x, y, flag):
    if x > y:
        return 0
    elif x == y:
        return 1
    elif flag:
        return f(x + 1, y, True) + f(x + 2, y, True) + f(x * 2, y, False)
    else:
        return f(x + 1, y, True) + f(x + 2, y, True)


print(f(1, 9, True))
