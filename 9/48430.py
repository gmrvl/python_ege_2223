file = open('csv-2.csv')
count = 0
fff = file.readline()
for i in file:
    a = i.split(',')
    a = list(map(int, a))
    # a = sorted(a)
    # if a[0] == a[1] and a[2] == a[3] and (a[4] != a[5]) and (a[4] != a[3]) and (a[1] != a[2]):
    #
    #     count += 1
    # elif a[0] == a[1] and a[2] == a[3] and (a[4] != a[5]) and (a[4] != a[3]) and (a[1] != a[2]):
    #     count += 1
    # elif a[0] == a[1] and a[2] == a[3] and (a[4] != a[5]) and (a[4] != a[3]) and (a[1] != a[2]):
    #     count += 1
    print(a)