a=[]
for i in range(1,10001):
    x = i
    l = 0
    m = 1
    while x > 0:
        l += 1
        if x%2 > 0:
            m *= x % 8
        x = x // 8
    if m == 25 and l==3:
        a.append(i)
print(max(a))
