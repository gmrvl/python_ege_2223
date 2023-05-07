def f(x, y, mult):  # переменная, означающая, что предыдущая команда была умножением
    if x > y:
        return 0
    elif x == y:
        return 1
    elif mult:
        return f(x + 1, y, False) + f(x + 2, y, False)
    else:
        return f(x + 1, y, False) + f(x + 2, y, False) + f(x * 2, y, True)


print(f(1, 11, False))
