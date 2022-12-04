for i in range(100,1000):
    n=str(i)
    a=int(n[0])*int(n[1])
    b=int(n[1])*int(n[2])
    n1=str(max(a,b))
    n2=str(min(a,b))
    s=n2+n1
    if s=='621':
        print(i)