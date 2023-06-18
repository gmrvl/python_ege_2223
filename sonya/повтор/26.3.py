file = open('26.3.txt')
N, M = map(int, file.readline().split())
count1 = 0
count2 = 0
summ1 = 0
n = []
for i in file:
    i = int(i)
    if 200 <= i <= 210:
        summ1 += i
        count1 += 1
    else:
        n.append(i)
n = sorted(n)
summ2 = []
for i in n:
    if i + sum(summ2) <= M - summ1:
        summ2.append(i)
        count2 += 1
    else:
        break
for k in range(1, count2):
    for i in range(count2 - k, len(n)):
        if (sum(summ2) - summ2[count2 - k] + n[i]) <= (M - summ1) and n[i] != 0:
            summ2[count2 - k] = n[i]
            n[i] = 0
print(count2 + count1, sum(summ2) + summ1)


