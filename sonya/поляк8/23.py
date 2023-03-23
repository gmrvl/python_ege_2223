# (№ 5217)
def f(x, y, mult):
    if x > y:
        return 0
    elif x == y:
        if mult <= 2:
            return 1
        else:
            return 0

    return f(x + 1, y, mult) + f(x * 2, y, mult + 1) + f(x * 3, y, mult + 1)


print(f(1, 100, 0))
