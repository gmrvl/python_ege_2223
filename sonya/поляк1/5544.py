def l(x):
    if x % 11 == 10:
        return '*'
    else:
        return x % 11


a = []
for i in range(0, 10):
    for j in range(0, 10):
        for p in range(0, 10):
            if i + j + p == 11:
                s = str(i) + str(j) + str(p)
                a.append(s)
a.append('000')
a.append('*01')
a.append('*10')
a.append('1*0')
a.append('0*1')
a.append('01*')
a.append('10*')
print(a)


def f(x, y, k):
    if x == y:
        k += '6'
        yes = False
        for i in range(0, len(a)):
            if a[i] in k:
                yes = True
                break
        if yes:
            return 1
        else:
            return 0
    if x > y:
        return 0
    return f(x + 2, y, k + str(l(x+2))) + f(x * 3, y, k + str(l(x*3))) + f(x * 4, y, k + str(l(x*4)))


print(f(1, 600, '1'))
