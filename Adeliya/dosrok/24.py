file=open('24.txt').read()
file=file.replace('Q','*')
file=file.replace('R','*')
file=file.replace('S','*')

count=0
maxx=0
last=''
for i in file:
    if i=='*' and last=='*':
        maxx=max(maxx,count)
        count=1
    else:
        count+=1
    last=i
print(maxx)