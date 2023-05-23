file = open('26-85.txt')
n = int(file.readline())
f = []

for i in file:
    ryad, mesto, gorod = map(int, i.split())
    f.append([ryad, mesto, gorod])

f = sorted(f)
new_f = []

for i in range(1, len(f)):
    if f[i-1][0] == f[i][0]:
        if f[i][1] - f[i - 1][1] == 101:
            if f[i][2] == f[i-1][2] == 1:
                new_f.append(f[i][0])
new_f = sorted(new_f, reverse=True)
print(new_f)
f = sorted(f, reverse=True)
for i in new_f:
    count = 0
    dr_goroda = 0
    for j in range(0, len(f)):
        if f[j][0] == i:
            if f[j][2] == 0:
                count += 1
            else:
                dr_goroda += 1
    if count > 500:
        print(i, dr_goroda)
