file=open('24.txt')
count=0
for i in file:
    if i.count('E')>i.count('A'):
        count+=1
print(count)