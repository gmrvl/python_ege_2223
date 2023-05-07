file=open('26.3.txt')
n, m = map(int, file.readline().split(' '))
b=[]
for i in file:
    s,k,t = i.split()
    s=int(s)
    k=int(k)
    if t=='A':
        m -= s*k
    else:
        b.append([s,k])
