file = open('27880.txt')
S, n = map(int, file.readline().split())
ns = [int(i) for i in file]
ns = sorted(ns)
s = 0
count = 0
for i in ns:
    if s + i <= S:
        s += i
        count += 1
    else:
        break
maxx = 0
for i in range(count, n):
    if (s - ns[count - 1]) + ns[i] <= S:
        maxx = ns[i]
    else:
        break
print(count, maxx)