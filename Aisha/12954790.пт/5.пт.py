for i in range(1000, 10000):
    first = i // 1000
    second = i // 100 % 10
    third = i // 10 % 10
    fourth = i % 10

    z = []

    z.append(first + second)
    z.append(second + third)
    z.append(third + fourth)

    z = sorted(z)
    res = str(z[1]) + str(z[2])
    if res == '1215':
        print(i)
        break
