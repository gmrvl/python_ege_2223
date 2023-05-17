for i in range(0,1000):
    n=bin(i)[2:]
    if i%3==0:
        n+=n[-3:]
    else:
        n+=bin(i%3*3)[2:]
    r=int(n,2)
    if r < 100:
        print(i)


