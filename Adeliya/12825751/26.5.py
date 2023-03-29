file=open('26.5.txt')
n=int(file.readline())
a=[]
for i in file:
    r,m=map(int, i.split())
    a.append([r,m])
a=sorted(a)
