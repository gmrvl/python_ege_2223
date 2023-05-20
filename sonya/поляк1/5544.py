def l(x):
    return x % 11
a = []
for i in range(0,10):
    for j in range(0, 10):
        for p in range(0, 10):
            if i + j + p == 11:
                s = str(i) + str(j) + str(p)
                a.append(s)
a.append('000')
print(a)
def f(x,y,k):
    if x == y:
        for i in range(0, len(a)):
            if a[i] in k:
                return 1
            else:
                return 0
    if x > y:
        return 0
    return f(x + 2,y, k + str(l(x+2))) + f(x * 3,y, k + str(l(x * 3))) + f(x * 4,y, k + str(l(x * 4)))
print(f(1,600, ''))