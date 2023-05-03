from fnmatch import*
for i in range(273, 10**8 + 1, 273):
    s = str(i)
    if fnmatch(s, '12??36*1'):
        print(i, i //273)
