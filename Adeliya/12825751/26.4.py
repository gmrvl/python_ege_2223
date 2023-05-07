file=open('26.4.txt')
s, n = map(int, file.readline().split(' '))
a = [int(i) for i in file]
a=sorted(a)
count=0
m=0
for i in a:
    if m+i <= s:
        count+=1
        m+=i
    else:
        break
maxx=0
for i in range(count,len(a)):
    if (s - a[count-1])+a[i] <= s:
        maxx=a[i]
    else:
        break
print(count,maxx)

