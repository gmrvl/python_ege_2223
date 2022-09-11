a=[]
for i in range(1,10001):
    for m in range(1,10001):
        s = i
        x = m
        s = 100*s + x
        n = 1
        while s < 2021:
            s = s + 5*n
            n = n + 1
        if n == 17:
            a.append(m)
print(min(a))