a=[]
for i in range (1,10001):
    s=i
    s = (s+15)//10
    n = 1
    while s >= 0:
        s = s - n
        n = n * 3
    if n==81:
        a.append(i)
print(min(a))




