def F(n):
    if n <= 1:
        return 0
    elif n % 2 == 1:
        return F(n-1) + 3 * n * n
    elif n % 2 == 0:
        return n/2 + F(n - 1) + 2
print(F(49))