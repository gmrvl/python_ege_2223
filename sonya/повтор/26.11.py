file = open('26.11.txt')
N = int(file.readline())
n = [int(i) for i in file]
n = sorted(n, reverse=True)
k = 0
maxx = 0
while len(n) > 0:
    count = [n.pop(0)]
    for i in range(len(n)):
        if count[-1] - n[i] >= 5:
            count.append(n[i])
            n[i] = ''
    n = [x for x in n if x != '']
    k += 1
    maxx = max(maxx, len(count))
print(k, maxx)