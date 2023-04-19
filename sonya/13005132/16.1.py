def F(n):
    if n == 1:
        return 2
    if n == 2:
        return 1
    else:
        return F(n-2) + F(n-1)
print(F(8))