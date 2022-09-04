w=[]
for i in range (1,10001):
    x=i
    a=0; b=1
    while x > 0:
        if x%2 > 0:
            a += x%8
        else:
            b = b * (x%8)
        x = x//8
    if a == 2 and b == 12:
        w.append(i)
print(max(w))