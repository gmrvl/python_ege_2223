def f(x,y):
    if x > y or x == 15:
        return 0
    elif x == y:
        return 1
    else:
        return f(x + 1, y) + f (x * 2, y)
print(f(1,10)*f(10,22))