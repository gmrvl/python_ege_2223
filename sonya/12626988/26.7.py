file = open('26.txt')
n = int(file.readline())
numbers = [int(i) for i in file]
chnumbers = []
for i in numbers:
    if i % 2 != 0:
        chnumbers.append(i)
count = 0
maxx = 0
ns = set(numbers)
for x in range(0, len(chnumbers) - 1):
    for y in range(x + 1, len(chnumbers)):
        srarf = (chnumbers[x] + chnumbers[y]) // 2
        if srarf in ns:
            count += 1
            maxx = max(maxx, srarf)
print(count, maxx)