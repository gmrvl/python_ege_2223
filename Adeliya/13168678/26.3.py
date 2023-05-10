file=open('26.3.txt')
n, maxsum = map(int, file.readline().split(' '))
data = []
for i in file:
    x, y = i.split()
    data.append([int(x), y])

alist = [k[0] for k in data if k[1] == 'A']
blist = [k[0] for k in data if k[1] == 'B']

alist.sort()
blist.sort()
data.sort()

msum = 0
maxc = 0

for i in data:
    if msum + i[0] <= maxsum:
        msum += i[0]
        maxc += 1
    else:
        break

buied_b = []

for i in blist:
    if len(buied_b) >= maxc: break
    if sum(buied_b) + i <= maxsum:
        buied_b.append(i)
    else:
        break

buied_a = []

for i in alist:
    if len(buied_b) + len(buied_a) >= maxc: break
    if sum(buied_b) + sum(buied_a) + i <= maxsum:
        buied_a.append(i)
    else:
        while sum(buied_b) + sum(buied_a) + i > maxsum:
            del buied_b[-1]
        buied_a.append(i)

print(len(buied_b))
print(maxsum - (sum(buied_b) + sum(buied_a)))
