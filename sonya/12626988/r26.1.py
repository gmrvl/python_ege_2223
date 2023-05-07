file = open('р26.1.txt')
numbers = [int(i) for i in file]
chnumbers = []
for i in numbers:
    if i % 2 == 0:
        chnumbers.append(i)
count = 0
maxx = 0
ns = set(numbers)
for x in range(0, len(chnumbers) - 1):
    for y in range(x + 1, len(chnumbers)):
        srarifm = (chnumbers[x] + chnumbers[y]) // 2
        if srarifm in ns:
            count += 1
            maxx = max(srarifm, maxx)
print(count, maxx)