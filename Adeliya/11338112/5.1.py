for i in range(100,1000):
    n=str(i)
    a=int(n[0])*int(n[1])
    b=int(n[1])*int(n[2])
    if a>b:
        n=str(b)+str(a)
    else:
        n=str(a)+str(b)
    if n=='621':
        print(i)