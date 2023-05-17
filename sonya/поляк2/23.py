def l(x):
    return str(x % 2)

def f(x,y,k):
    if x == y and not '11' in k:
        return 1
    if x > y:
        return 0
    return f(x + 2, y, k + l(x + 2)) + f(x * 3,y, k + l(x * 3)) + f(x*4, y, + k + l(x * 4))
print(f(1,600, ''))
