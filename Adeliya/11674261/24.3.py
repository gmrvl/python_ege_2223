# Текстовый файл состоит из символов P, Q, R и S.
# Определите максимальное количество идущих подряд символов в прилагаемом файле, среди которых нет идущих подряд символов P.
file=open('24.3.txt')
count=0
maxcount=0
s = str(file.readline())
for i in range(0,len(s)):
    if s[i]=='P' and s[i+1]=='P':
        count=0
    else:
       count+=1
if count> maxcount:
    maxcount=count
print(maxcount)


