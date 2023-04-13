file = open('р26.2.txt')
S, N = map(int, file.readline().split())
n = [int(i) for i in file]
s = 0
count = 0
n = sorted(n)

for i in n:
    if s + i <= S:
        s += i
        count += 1

maxx = 0
for i in range(count, N):
    if (s - n[count - 1]) + n[i] <= S:
        maxx = n[i]

print(count, maxx)