for i in range(1,101):
    n=str(bin(i)[2:])
    if i%2==0:
        n+='01'
    else:
        n+='10'
    r=int(n,2)
    if r>102:
        print(r)
        break