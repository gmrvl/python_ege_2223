def l(x):
    return str(x).count('1') + str(x).count('2') * 2 + str(x).count('3') * 3 + str(x).count('4') * 4 + str(x).count('5') * 5 + str(x).count('6') * 6 + str(x).count('7') * 7 + str(x).count('8') * 8 + str(x).count('9') * 9


def f(x,y,k):
    if x == y and k == 5:
        return 1
    elif x > y:
        return 0
    else:
        if l(x + 2) == 14 and l(x * 3) == 14 and l(x * 4) == 14:
            return f(x + 2, y, k + 1) + f(x * 3, y, k + 1) + f(x * 4,y , k + 1)
        elif l(x + 2) != 14 and l(x * 3) == 14 and l(x * 4) == 14:
            return f(x + 2, y, k) + f(x * 3, y, k + 1) + f(x * 4,y,  k + 1)
        elif l(x + 2) != 14 and l(x * 3) != 14 and l(x * 4) == 14:
            return f(x + 2, y, k) + f(x * 3, y, k) + f(x * 4, y, k + 1)
        elif l(x + 2) != 14 and l(x * 3) == 14 and l(x * 4) != 14:
            return f(x + 2, y, k) + f(x * 3, y, k + 1) + f(x * 4, y,  k)
        else:
            return f(x + 2, y, k) + f(x * 3, y, k) + f(x * 4,y,  k)
print(f(1,600, 0))