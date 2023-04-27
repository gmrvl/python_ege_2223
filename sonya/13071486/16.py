def F(n):
    if n <= 2:
        return 2
    else:
        return F(n - 1) * F(n - 2)
print(F(5))