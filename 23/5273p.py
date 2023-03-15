def f(x, y, mult5, mult3, plus45):
    if x > y:
        return 0
    if x == y:
        return 1
    elif mult5 < 4:
        if mult3 < 2:
            if plus45 < 5:
                mult5 += 1
                mult3 += 1
                plus45 += 1
                print(f(x * 5, y, mult5, mult3, plus45) + f(x * 3, y, mult5, mult3, plus45) + f(x + 45, y, mult5,
                                                                                                mult3, plus45))
                return f(x * 5, y, mult5, mult3, plus45) + f(x * 3, y, mult5, mult3, plus45) + f(x + 45, y, mult5,
                                                                                                 mult3, plus45)

            else:
                mult5 += 1
                mult3 += 1
                return f(x * 5, y, mult5, mult3, plus45) + f(x * 3, y, mult5, mult3, plus45)
        else:
            if plus45 < 5:
                mult5 += 1
                mult3 += 1
                plus45 += 1
                return f(x * 5, y, mult5, mult3, plus45) + f(x * 3, y, mult5, mult3, plus45) + f(x + 45, y, mult5,
                                                                                                 mult3, plus45)
            else:
                mult5 += 1
                mult3 += 1
                return f(x * 5, y, mult5, mult3, plus45) + f(x * 3, y, mult5, mult3, plus45)
    else:
        if mult3 < 2:
            if plus45 < 5:
                mult3 += 1
                plus45 += 1
                return f(x * 3, y, mult5, mult3, plus45) + f(x + 45, y, mult5,
                                                             mult3, plus45)
            else:
                mult3 += 1
                return f(x * 3, y, mult5, mult3, plus45)
        else:
            if plus45 < 5:
                mult3 += 1
                plus45 += 1
                return f(x * 3, y, mult5, mult3, plus45) + f(x + 45, y, mult5,
                                                             mult3, plus45)
            else:
                mult3 += 1
                return f(x * 3, y, mult5, mult3, plus45)


print(f(1, 2970, 0, 0, 0))
