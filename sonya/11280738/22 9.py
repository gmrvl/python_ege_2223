w=[]
for i in range(1,10001):
    x=i
    a = 0
    b = 1
    while x > 0:
        a += 1
        b *=x % 10
        x //=  10
    if a==2 and b==0:
        w.append(i)
print (max(w))