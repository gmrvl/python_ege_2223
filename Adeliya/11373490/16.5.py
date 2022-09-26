def F(n):
    if n==0:
        return 0
    if n>0 and n%3==0:
        return F(n//3)
    if n%3>0:
        return  n%3 + F(n-(n%3))
i=0
while F(i) !=9:
    i+=1
print(i)