from fnmatch import*
for n in range(273, 10**8, 273):
    if fnmatch(str(n), '12??36*1'):
        print(n, n //273)