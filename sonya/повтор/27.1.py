file = open('1_27_A.txt')
K = int(file.readline())
N = int(file.readline())
n = [int(i) for i in file]
maxx = 0
summ = 0
for i in range(len(n)):
    maxx = max(maxx, n[i])
    if i + K < len(n):
        summ = max(summ, maxx + n[i + K])
print(summ)
