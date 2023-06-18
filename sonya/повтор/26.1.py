file = open('26.1.txt')
S, N = map(int, file.readline().split())
n = [int(i) for i in file]
n = sorted(n)
s = 0
count = 0
for i in n:
    if s + i <= S:
        count += 1
        s += i
    else:
        break

maxx = 0
for i in range(count - 1, len(n)):
    if (s - n[count - 1]) + n[i] <= S:
        maxx = n[i]
    else:
        break
print(count, maxx)

