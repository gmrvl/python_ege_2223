file = open('26.3.txt')
n = int(file.readline())
ns = []
for i in file:
    x, y = map(int,file.readline().split())
    ns.append([x,y])
ns = sorted(ns)
print(ns)
count = 0