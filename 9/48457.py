file=open('')
count=0
for i in file:
    a=list(map(int, i.split(';')))
    a=sorted(a)
    if a[0]==a[1] and a[2]==a[3] and a[4]!=a[5] and a[1]!=a[2] and a[3]!=a[4]:
        if a[1]+a[2] > a[4]+a[5]:
            count+=1
    elif a[1] == a[2] and a[3] == a[4] and a[0] != a[5] and a[3] != a[2] and a[5] != a[4] and a[0] != a[1]:
        if a[1]+a[3] > a[0]+a[5]:
            count+=1
    elif a[2] == a[3] and a[4] == a[5] and a[0] != a[1] and a[3] != a[4] and a[2] != a[1]:
        if a[2]+a[4] > a[0]+a[1]:
            count+=1
print(count)
