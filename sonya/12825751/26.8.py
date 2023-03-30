file = open('26.8.txt')
n = int(file.readline())
a = [int(i) for i in file]
a = sorted(a, reverse=True)
count = 0
pod = [a[0]]
for i in range(1, len(a)):
    if pod[-1] - a[i] >= 3:
        count += 1
        pod.append(a[i])
print(count, pod[-1])