file = open('26.1.txt')
S, N = map(int, file.readline().split())
ns = [int(i) for i in file]
ns = sorted(ns)
s = 0
count = 0
for i in ns:
    if s + i <= S:
        count += 1
        s += i
    else:
        break
msxx = 0
for i in range(count, len(ns)):
    if (s - ns[count - 1]) + ns[i] <= S:
        maxx = ns[i]
    else:
        break
print(count, maxx)
