count = 0
n = 200000001
while count < 5:
    a = []
    sq = int(n ** 0.5)
    for i in range(2, sq + 1):
        if n % i == 0:
            a.append(i)
            a.append(n // i)
    if len(a) >= 5:
        m=a[0]+a[1]+a[2]+a[3]+a[4]
    else:
        m=0
    if 0 < m < n:
        print(m)
        count+=1


