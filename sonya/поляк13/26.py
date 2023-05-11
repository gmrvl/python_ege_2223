file = open('26-94.txt')
N, K = map(int, file.readline().split())
a = []
for i in file:
    x, ryad, mesto = map(int, i.split())
    a.append([x, ryad, mesto])
a = sorted(a)
print(a)
count = 0
for i in range(1, len(a)):
    if a[i-1][2] == 1 or a[i-1][2] == 2 or a[i-1][2] == 5 or a[i-1][2] == 6:
        count += 1
        if a[i-1][0] == a[i][0]:
            if a[i-1][1] == a[i][1]:
                if (a[i-1][2] == 5 and a[i][2] != 6) or (a[i-1][2] == 6 and a[i][2] != 5) or (a[i-1][2] == 1 and a[i][2] != 2) or (a[i-1][2] == 2 and a[i][2] != 1):
                    count -= 1
print(count)
