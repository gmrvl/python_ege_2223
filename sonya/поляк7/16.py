from functools import*
@lru_cache(None)
def F(n):
    if n < 3:
        return 1
    summ = 0
    for i in str(n):
        summ += int(i)
    if summ % 2 == 0:
        return F(n - 1) - F(n - 2)
    return F(n - 1) + F(n // 2)
print(F(100))