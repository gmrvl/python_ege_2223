file = open('26.2.txt')
S, n = map(int, file.readline().split())
files = [int(i) for i in file]
files = sorted(files)

count = 0
maxfile = 0
s = 0

for i in files:
    if s + i <= S:
        s += i
        count += 1
    else:
        break

for i in range(count, n):
    if (s - files[count - 1]) + files[i] <= S:
        maxfile = files[i]
    else:
        break
print(count, maxfile)