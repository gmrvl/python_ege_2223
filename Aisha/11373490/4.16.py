def F(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return F(n-2)
print(F(7))