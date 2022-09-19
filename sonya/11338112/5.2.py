for i in range(2,1000):
    n = str(bin(i))
    n = n + str(n[3])+ str(n[2])
    n = int(n,2)
    if n > 74:
        print(i)
