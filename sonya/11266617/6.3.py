a=[]

for i in range (1,1001):
    for w in range(1, 1001):
        s = i
        x = w
        s = 100*s + x
        n = 1
        while s < 2021:
            s = s + 5*n
            n = n + 1
        if n == 15:
            a.append(w)
print(min(a))