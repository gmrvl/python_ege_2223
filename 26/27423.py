file = open('27423.txt')
s, n = map(int, file.readline().split())
files = []
for i in file:
    files.append(int(i))
files = sorted(files)

arch = 0
count = 0
for file in files:
    if arch + file <= s:
        arch += file
        count += 1
    else:
        break
arch -= files[count-1]
maxFile = 0
for i in range(count, len(files)):
    if arch + files[i] <= s:
        maxFile = files[i]
    else:
        break
print(count, maxFile)

