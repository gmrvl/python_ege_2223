count=0
for i in range(1,1000):
    n=bin(i)[2:]
    if int(n)%2==0:
        n1='1'+n+'10'
    else:
        n1='11'+n+'0'
    r=int(n1,2)
    if 800 <= r <= 1500:
        count+=1
print(count)