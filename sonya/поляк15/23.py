def l(x):
    return int(x % 6 == 0)

def f(x, y, k):
    if x == y and k <= 4:
        return 1
    if x > y:
        return 0
    return f(x + 2, y, k + l(x + 2)) + f(x * 2, y, k + l(x * 2)) + f(x * 3, y, k + l(x * 3))
print(f(1,300, 0))