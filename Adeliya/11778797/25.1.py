count=0
n=11000001
while count <5:
    a=[]
    sq=int(n**0.5)
    for i in range(2,sq+1):
        if n % i == 0:
            a.append(i)
        if len(a) >= 2:
            break