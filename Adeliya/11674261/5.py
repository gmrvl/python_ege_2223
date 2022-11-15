for i in range(1,1001):
    n=bin(i)[2:]
    summ=(n.count('1'))
    if summ%2==0:
        n+='00'
    else:
        n+='10'
    r=int(n,2)
    if r>125:
        print(i)
        break
