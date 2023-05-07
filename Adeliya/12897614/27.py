file=open('27_B.txt')
n=int(file.readline())

a = []
for i in file:
    number, prob = map(int, i.split())
    if prob % 36 == 0:
        a.append([number,prob//36])
    else:
        a.append([number, prob // 36+1])


min_sum = 10 ** 100000

total_prob = [a[0][1]]
for i in range(1, n):
    total_prob.append(total_prob[i-1] + a[i][1])

s = 0
for i in range(1, n):
    s += abs(a[0][0] - a[i][0]) * a[i][1]


for i in range(1, n):
    s = s + (a[i][0] - a[i-1][0]) *  total_prob[i-1]- (a[i][0] - a[i-1][0]) * (total_prob[-1] - total_prob[i-1])
    min_sum = min(s, min_sum)
print(min_sum)
