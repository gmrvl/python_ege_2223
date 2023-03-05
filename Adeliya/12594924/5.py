for i in range(1,1000):
    n=str(bin(i)[2:])
    if n.count('1')>n.count('0'):
        n+='1'
    else:
        n+='0'
    r=int(n,2)
    if r > 100:
        print(r)
        break

