def f(x,h):
    if h == 5:
        a.add(x)
    else:
        f(x + 1, h + 1)
        f(x * 2, h + 1)

a = set()
f(1,0)
print(a)