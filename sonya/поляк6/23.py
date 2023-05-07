def f(x,y):
    if x == y:
        return 1
    if x > y:
        return 0
    else:
        return f(x*5,y) + f(x*3,y) + f(x+45,y)
print()