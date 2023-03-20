def F(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return F(n - 1)+n

print(F(40))
