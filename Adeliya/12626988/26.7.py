file = open('26.7.txt')
n = file.readline()
a = []
for i in file:
    a.append(int(i))
count = 0
maxx = 0
s = 0
b = set(a)
for i in range(0, len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i] % 2 != 0 and a[j] % 2 != 0:
            s = (a[i] + a[j]) // 2
            if s in b:
                count += 1
                if s > maxx:
                    maxx = s
print(count, maxx)
