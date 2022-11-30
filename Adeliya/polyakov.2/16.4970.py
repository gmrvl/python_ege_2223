from functools import cache


@cache
def F(n):
    if n == 0:
        return 8
    if n > 0 and n % 3 == 0:
        return 5 + F(n / 3)
    else:
        return F(n // 3)


k = 0
for n in range(1, 100000000):
    if F(n) == 18:
        k += 1
        print(n)
print(k)
