for i in range(0,10):
    a=int('4C'+str(i)+'4',15)
    b=int(str(i)+'62A',13)
    s=a+b
    if s%121==0:
        print(s//121)