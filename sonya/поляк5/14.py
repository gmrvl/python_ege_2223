a = []
for x in range(0,13):
    for y in range(0, 13):
        M = int('2' + str(y) + '23' + str(x) + '5', 15)
        N = int('67' + str(x) + '9' + str(y), 13)
        for A in range(1,10000):
            if (M + A) % N == 0:
                a.append(A)
print(min(a))
