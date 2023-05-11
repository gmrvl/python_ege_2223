def l(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return int(sum == 14)


def f(x, y, k):
    if x == y and k == 5:
        return 1
    elif x > y:
        return 0
    else:
        return f(x + 2, y, k + l(x + 2)) + f(x * 3, y, k + l(x * 3)) + f(x * 4, y, k + l(x * 4))


print(f(1, 600, 0))
