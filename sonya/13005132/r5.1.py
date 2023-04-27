for n in range(100,1000):
    n = str(n)
    a = int(n[0]) * int(n[1])
    b = int(n[1]) * int(n[2])
    r = str(min(a,b)) + str(max(a,b))
    if r == '621':
        print(n)

