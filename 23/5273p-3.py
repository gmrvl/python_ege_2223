def f(x, y, c5, c3, c45):
    if x > y:
        return 0
    elif x == y:
        if c5 <= 4 and c3 >= 2 and c45 == 5:
            return 1
        else:
            return 0
    else:
        return f(x * 5, y, c5 + 1, c3, c45) + f(x * 3, y, c5, c3 + 1, c45) + f(x + 45, y, c5, c3, c45 + 1)


print(f(1, 2970, 0, 0, 0))
