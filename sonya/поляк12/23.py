def f(x,y,k):
    if x > y:
        return 0
    if x == y and k <= 5:
        return 1
    else:
        return f(x + 1, y, k) + f(x * 3, y, k + 1) + f(x * 4, y, k + 1)
print(f(3,300,0))