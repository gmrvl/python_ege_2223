def M(N):
    k = 0
    dell = 0
    maxdell = 0
    sqn = int(N ** 0.5)
    for i in range(1, sqn + 1):
        if N % i == 0:
            k += 1
            dell = N // i
            if maxdell < dell:
                maxdell = dell
    if k < 2:
        return 0
    else:
        return (N // maxdell) + (N // (N // maxdell))

count = 0
n = 11000000
while count < 5:
    number = n
    if 0 < M(n) < 10000:
        print(M(n), number)
        count += 1
    n += 1