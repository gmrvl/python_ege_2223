def f(x,y):
    if x>y:
        return 0
    if x==y:
        return 1
    else:
        return f(x+1,y)+f(x*3,y)+f(x+2,y)
print(f(1,10)*f(10,12)*f(12,15))