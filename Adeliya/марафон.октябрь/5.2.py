for i in range(10000,100000):
    n=str(i)
    a=int(n[0])+ int(n[2]) + int(n[4])
    b=int(n[1]) + int(n[3])
    n1= str(max(a,b))
    n2= str(min(a,b))
    s = n2 + n1
    if s=='621':
        print(i)
        break
