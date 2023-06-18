file = open('27880.txt')
S ,N = map(int, file.readline().split())
n = [int(i) for i in file]
n = sorted(n)

count = 0
s = 0
for i in n:
    if s + i <= S:
        count += 1
        s += i
maxx = 0
s0 = s - n[count - 1]
for i in range(count, len(n)):
    if (s0 + n[i]) <= S:
        maxx = n[i]
print(count, maxx)
