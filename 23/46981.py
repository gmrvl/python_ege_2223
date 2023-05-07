def F(x, y, flag):
    if x > y:
        return 0
    elif x == y:
        return 1
    elif flag:
        return F(x + 1, y, True) + F(x + 2, y, True) + F(x * 2, y, False)
    else:
        return F(x + 1, y, True) + F(x + 2, y, True)


print(F(1, 11, True))
