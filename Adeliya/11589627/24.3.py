file=open('24.3.txt')
count=0
for i in file:
    if i.count('A') > i.count('E'):
        count+=1
print(count)