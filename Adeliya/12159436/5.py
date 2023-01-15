for i in range(1,1000):
    n=str(bin(i)[2:])
    if i%2==0:
        n+='00'
    else:
        n+='11'
    r=int(n, 2)
    if r<94:
        print(i)