def F(n):
    if n==1:
        return 1
    if n>1:
        return n*F(n - 1) - 1
print(F(1000)/F(997))