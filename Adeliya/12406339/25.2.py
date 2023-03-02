a=[]
for m in range(2,100,2):
    for n in range(1,101,2):
        N = 2 ** m * 3 ** n
        if 200000000<=N<=400000000:
            a.append(N)
a=sorted(a)
print(a)
