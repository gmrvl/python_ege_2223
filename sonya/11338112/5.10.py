

for i in range(1,1000):
    n = str(bin(i)[2:])
    s1 = n.count('1')
    s0 = n.count('0')
    if s1 == s0 :
        n = n + str(n[-1])
    elif s1 > s0:
        n = n + '0'
    else:
        n = n + '1'
    if s1 == s0 :
        n =  n + str(n[-1])
    elif s1 > s0:
        n = n+ '0'
    else:
        n = n + '1'
    if s1 == s0 :
        n = n + str(n[-1])
    elif s1 > s0:
        n = n + '0'
    else:
        n = n + '1'
    r = int(n,2)
    if i >99 and r%4==0:
        print(i)