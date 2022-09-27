def F(n):
    if n==1:
        return 1
    if n==2:
        return 1
    if n >2:
        return F(n - 2) * n
print(F(7))
