def F(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return F(n - 1) * F(n - 2) + (n - 2)

print(F(5))
