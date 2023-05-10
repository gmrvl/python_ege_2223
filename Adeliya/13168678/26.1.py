file=open('26.1.txt')
n, maxsum = map(int, file.readline().split(' '))
data = []
for i in file:
    x, k, y = i.split()
    data.append([int(x),int(k), y])

alist = [k[0] for k in data if k[2] == 'A']
blist = [k[0] for k in data if k[2] == 'B']

alist.sort()
blist.sort()
data.sort()

print(alist)
print(blist)
print(data)