file=open('26.6.txt')
n = int(file.readline())
a = []
for i in file:
    r, m = map(int, i.split())
    a.append([r, m])
a = sorted(a)

for i in range(1,len(a)):
    if a[i][0]==a[i-1][0]:


