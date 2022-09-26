def F(n):
    if n==1:
        return 1
    if n==2:
        return  2
    if n==3:
        return 3
    if n > 3:
        return F(n - 3)*n
print(F(11))