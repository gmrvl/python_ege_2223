for i in range(1000, 10000):
    first = i // 1000
    second = i // 100 % 10
    third = i // 10 % 10
    fourth = i % 10
    a = []
    a.append(first + second)
    a.append(second + third)
    a.append(third + fourth)

    a = sorted(a)
    res = str(a[1]) + str(a[2])

    if res == '1315':
        print(i)
        break