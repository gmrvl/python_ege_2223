file = open('26.2.txt')
N = int(file.readline())
summ = 0
n = []
for i in file:
    i = int(i)
    if i < 51:
        summ += i
    else:
        n.append(i)
n = sorted(n)
k = len(n) // 2
maxx = 0
for i in range(0, k):
    summ += n[i]*0.75
    maxx = n[i]
for i in range(k, len(n)):
    summ += n[i]
print(summ, maxx)
