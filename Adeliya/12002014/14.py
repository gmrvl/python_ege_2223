a=2*216**8 + 4*36**12 + 6**15 - 1296
count=0
while a!=0:
    if a%6==0:
        count+=1
    a//=6
print(count)