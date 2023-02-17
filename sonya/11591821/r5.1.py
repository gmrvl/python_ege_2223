for i in range(10000, 100000):
    n = str(i)
    a = int(n[0]) + int(n[2]) + int(n[4])
    b = int(n[1]) + int(n[3])
    if a > b:
        n = str(b) + str(a)
    else:
        n = str(a) + str(b)
    if n == '621':
        print(i)
        break

