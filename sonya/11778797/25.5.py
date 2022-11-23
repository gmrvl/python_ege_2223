maxdels = 0
N = []
for n in range(568023, 569231):
    sqn = int(n ** 0.5)
    dels = 0
    for d in range(1,sqn + 1):
        if n % d == 0:
            if (n // d) == d:
                dels += 1
            else:
                dels += 2
    if maxdels < dels:
        maxdels = dels
        N = []
        N.append(n)
    if maxdels == dels:
        N.append(n)
print(maxdels, N)
