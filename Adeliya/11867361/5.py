for i in range(105,1000):
    n=str(bin(i)[2:])
    for j in range(3):
        if n.count('1')==n.count('0'):
            n+=n[-1]
        if n.count('1')>n.count('0'):
            n+='0'
        else:
            n+='1'
    r=int(n,2)
    if r%4==0:
        print(i)
        break


