file = open('27887.txt')
S, N = map(int, file.readline().split())
ns = [int(i) for i in file]
ns = sorted(ns)
count = 0
s = 0
for i in ns:
    if s + i <= S:
        count += 1
        s += i
    else:
        break
maxx = 0
for i in range(count, N):
    if (s - ns[count - 1]) + ns[i] <= S:
        maxx = ns[i]
    else:
        break
print(count, maxx)