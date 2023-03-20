
for i in range (100, 1000):
    i = str(i)
    first = int(i[0])
    second = int(i[1])
    third = int(i[2])

    n = first *  second
    c = second * third

    z = str(max(n,c))
    w = str(min(n,c))

    res = z + w
    if res == '205':
        print(i)
        break