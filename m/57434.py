file = open('1_27_A.txt')

k = int(file.readline())
n = int(file.readline())
a = []
for i in file:
    a.append(int(i))
maxx = 0
for i in range(0, len(a) - k):
    for j in range(i + k, len(a)):
        if a[i] + a[j] > maxx:
            maxx = a[i] + a[j]
print(maxx)
