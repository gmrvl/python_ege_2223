file=open('26.txt')
k=file.readline()
n=file.readline()
a=[]
for i in file:
    ts,tv=map(int,i.split())
    a.append([ts,tv])
a=sorted(a)