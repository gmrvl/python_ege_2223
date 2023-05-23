file = open('09.csv')
count = 0
for i in file:
    a = list(map(int, i.split(';')))
    a = sorted(a)
    if a[0] != a[1] != a[2] != a[3] != a[4]:
        if (a[0] + a[4])*3 <= (a[1] + a[2] + a[3])*2:
            count += 1
print(count)
