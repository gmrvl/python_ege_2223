file=open('27_B.txt')
n = int(file.readline())
data = []
for i in file:
    point, prob = map(int, i.split())
    if prob % 36 == 0:
        k = prob // 36
    else:
        k = prob // 36 + 1
    data.append([point, k])

min_sum = 10 ** 1000000
total_prob = [data[0][1]]

for i in range(1, n):
    total_prob.append(total_prob[i-1] + data[i][1])

s = 0
for i in range(1, n):
    s += abs(data[0][0] - data[i][0]) * data[i][1]

for i in range(1, n):
    s = s + total_prob[i-1] * (data[i][0] - data[i-1][0]) - (data[i][0] - data[i-1][0]) * (total_prob[-1] - total_prob[i-1])
    min_sum = min(s, min_sum)

print(min_sum)