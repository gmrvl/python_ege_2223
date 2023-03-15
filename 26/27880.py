file = open('27880.txt')
s, n = map(int, file.readline().split())
files = []

for i in file:
    files.append(int(i))
files = sorted(files)
summ = 0
c = 0
for i in range(len(files)):
    if files[i] + summ <= s:
        summ += files[i]
    else:
        print(i)
        c = i
        break
maxx = 0
for i in range(c, n):
    if (summ - files[c - 1]) + files[i] <= s:
        maxx = files[i]
    else:
        break
print(c, maxx)

