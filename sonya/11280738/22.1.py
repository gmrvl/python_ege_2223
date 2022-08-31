w=[]

for i in range (1,10001):
    x=i
    a=0; b=10
    while x > 0:
        d = x % 6
        if d > a: a = d
        if d < b: b = d
        x = x // 6
    if a*b==12:
        w.append(i)
print(min(w))