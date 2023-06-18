file = open('26.5.txt')
N = int(file.readline())
n = [int(i) for i in file]
nechet = []
for i in n:
    if i % 2 == 1:
        nechet.append(i)
n = set(n)
count = 0
srarifm = []
for x in range(0, len(nechet) - 1):
    for y in range(x + 1, len(nechet)):
        if (nechet[x] + nechet[y])//2 in n:
            count += 1
            srarifm.append((nechet[x] + nechet[y])//2)
print(count, max(srarifm))