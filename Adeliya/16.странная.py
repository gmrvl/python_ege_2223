def F(n):
    if n==0:
        return 0
    else:
        return F(n-1)+n
c=0
for n in range(765432010,1542613235):
    if F(n)%3 !=0:
        c+=1
print(c)