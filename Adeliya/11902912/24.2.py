file=open('24.2.txt')
a=file.readline()
maxcount=0
alth='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in alth:
    count=0
    for j in range(len(a)-2):
        if a[j]==a[j+2] and a[j+1]==i:
            count+=1
    if count>maxcount:
        maxcount=count
print(i)