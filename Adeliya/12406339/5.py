for i in range(0,1000):
    n=str(bin(i)[2:])
    summ=n.count('1')
    if summ%2==1:
        n+='10'
    else:
        n+='00'
    r=int(n,2)
    if r>77:
        print(i)
        break
