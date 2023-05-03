from fnmatch import*
ns = []
for n in range(2023, 10**8, 2023):
    n = str(n)
    if fnmatch(n, '11????11'):
        if int(n[2]) % 2 == 0 and int(n[5]) % 2 != 0:
            print(n, int(n) // 2023)