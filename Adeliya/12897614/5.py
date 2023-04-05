for i in range(1000,10000):
    n=str(i)
    a=int(n[0]) + int(n[1])
    b=int(n[2])+int(n[3])
    n1=str(max(a,b))
    n2=str(min(a,b))
    s=n2+n1
    if s=='117':
        print(i)