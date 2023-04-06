file = open('27-B.txt')
files = [int(i) for i in file]
files = sorted(files)
count = 0
countch = 0
for n in range(0, len(files)):
    if files[n] % 2 == 0:
        countch += 1
    count += files[n]
files = sorted(files, reverse=True)
for n in range(0, len(files)):
    if countch % 10 != 0:
        if files[n] % 2 == 0:
            countch = countch - 1
        count = count - files[n]
    else:
        print(count)
        break
