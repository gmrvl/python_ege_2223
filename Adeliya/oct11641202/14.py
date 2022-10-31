a= 36**8+6**20-12
count=0
while a!=0:
    if a%6==0:
        count+=1
    a//=6
print(count)
