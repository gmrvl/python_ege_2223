for i in range(1000,10000):
    n=str(i)
    a=int(n[0])+int(n[1])
    b=int(n[1])+int(n[2])
    c=int(n[2])+int(n[3])
    n1 = str(a + b + c - max(a, b, c) - min(a, b, c))
    n2 = str(max(a, b, c))
    s=n1+n2
    if s=='1517':
        print(i)
