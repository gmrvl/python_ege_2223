file = open('26.3.txt')
S, n = map(int, file.readline().split())
files = [int(i) for i in file]
files = sorted(files)
s = 0
count = 0
for i in files:
    if i + s <= S:
        s += i
        count += 1
    else:
        break
maxx = 0
for i in (count, len(files)):
    if (s - files[count - 1]) + files[i] <= S:
        maxx = files[i]
    else:
        break
print(count, maxx)