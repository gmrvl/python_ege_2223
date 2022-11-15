a = [] #переписать по логике из первой задачи
for i in range(210235, 210301):
    k = 0
    sq = int(i ** 0.5)
    for n in range(2, sq):
        if i % n == 0:
            k += 1
    if k == 2:
        a.append(i)
print(a)


s1 = a[0]
s2 = a[1]
s3 = a[2]
dells1 = []
dells2 = []
dells3 = []

for dell in range(2, int(s1 ** 0.5)):
    if s1 % dell == 0:
        dells1.append(dell)
        dells1.append(s1 // dell)

for delll in range(2,int(s2 ** 0.5)):
    if s2 % delll == 0:
        dells2.append(delll)
        dells2.append(s2 // delll)

for dellll in range(2,int(s3 ** 0.5)):
    if s3 % dellll == 0:
        dells3.append(dellll)
        dells3.append(s3 // dellll)

print(dells1,dells2,dells3)