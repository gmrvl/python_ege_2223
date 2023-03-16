def f(x, y, mult5, mult3, plus45):
    if x > y:
        return 0
    if x == y:
        if mult5 <= 4 and mult3 >= 2 and plus45 == 5:
            return 1
        else:
            return 0
    elif mult5 < 4:
        if mult3 < 2:
            if plus45 < 5:
                return f(x * 5, y, mult5 + 1, mult3, plus45) + f(x * 3, y, mult5, mult3 + 1, plus45) + f(x + 45, y, mult5,
                                                                                                 mult3, plus45 + 1)
            else:
                return f(x * 5, y, mult5 + 1, mult3, plus45) + f(x * 3, y, mult5, mult3 + 1, plus45)
        else:
            if plus45 < 5:
                return f(x * 5, y, mult5 + 1, mult3, plus45) + f(x * 3, y, mult5, mult3 + 1, plus45) + f(x + 45, y, mult5,
                                                                                                 mult3, plus45 + 1)
            else:
                return f(x * 5, y, mult5 + 1, mult3, plus45) + f(x * 3, y, mult5, mult3 + 1, plus45)
    else:
        if mult3 < 2:
            if plus45 < 5:
                return f(x * 3, y, mult5, mult3 + 1, plus45) + f(x + 45, y, mult5, mult3, plus45 + 1)
            else:
                return f(x * 3, y, mult5, mult3 + 1, plus45)
        else:
            if plus45 < 5:
                return f(x * 3, y, mult5, mult3 + 1, plus45) + f(x + 45, y, mult5, mult3, plus45 + 1)
            else:
                return f(x * 3, y, mult5, mult3 + 1, plus45)


print(f(1, 2970, 0, 0, 0))
