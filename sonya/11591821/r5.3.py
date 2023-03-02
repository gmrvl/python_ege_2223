for n in range(1000, 10000):
    r = str(n)
    a = []
    a.append(int(r[0]) + int(r[1]))
    a.append(int(r[1]) + int(r[2]))
    a.append(int(r[2]) + int(r[3]))
    a.sort()
    r = str(a[-2]) + str(a[-1])
    if r == '1517':
        print(n)
        break
