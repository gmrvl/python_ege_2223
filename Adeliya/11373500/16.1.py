def F(n):
    if n==0:
        return 0
    if n%3==0 and n>0:
        return n + F(n - 3)
    if (n%3)>0:
        return n + F(n - (n%3))
print(F(22))