for i in range(1,1000):
    n=str(bin(i)[2:])
    n+=str(n.count('1')%2)
    n += str(n.count('1') % 2)
    r=int(n,2)
    if r < 90:
        print(r)






