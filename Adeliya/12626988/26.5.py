file=open('26.5.txt')
n = file.readline()
a=[]
for i in file:
    x,y=map(int, i.split(' '))
    a.append([x,y])
a=sorted(a)
