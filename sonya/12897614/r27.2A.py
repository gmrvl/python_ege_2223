file = open('р27.2_B.txt')
n = int(file.readline())
ns = [int(i) for i in file]
count = 0
for x in range(0,len(ns) - 1):
    for y in range(x + 1, len(ns)):
        if (ns[x] * ns[y]) % 26 == 0:
            count += 1
print(count)