import sys

def F(n):
    if n == 0:
        return 0
    if 1 <= n < 3:
        return 1
    if n >= 3:
        return F(n - 1) + F(n - 2)


print(F(47))
