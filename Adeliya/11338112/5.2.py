for i in range(2,1001):
    n=bin(i)[2:]
    n=str(n)
    n += n[1]+n[0]
    r = int(n,2)
    if r>74:
        print(i)
        break



