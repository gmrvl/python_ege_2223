for i in range(52, 1, -1):
    if (166212 + 55*54*i - 2*(55**3)) % 29 == 0:
        print(i)

a = 166212 + 55*54*40 - 2*(55**3)
minn = 100000000000000000000
for z in range(55):
    for x in range(55):
        for y in range(55):
            for a in range(55):
                k = ((55**2)*a + 55*y + x - (2*(55**3) + x*(55*2) + 55*a + y))
                if k % 29 == 0 and k < minn:
                    minn = k
                    print(k)
print(a)
print(abs(a-minn))


