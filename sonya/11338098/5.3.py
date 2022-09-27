
for i in range(1,1001):
    n = ''
    while i >0:
        n = str(i % 3) + n
        i //=3
    n = n + n[-1]
    n = int(n,3)
    if 100 <= n <= 999:
        print(n)