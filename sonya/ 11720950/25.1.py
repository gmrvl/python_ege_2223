a = []
for i in range(174457, 174506):
    sq = int(i ** 0.5)
    k = 0
    for dell in range(2, sq):
        if i % dell == 0:
            k += 1
    if k == 1:
        a.append(i)
print(a)

delll = []
delll2 = []
for n in a:
    sq = int(n ** 0.5)
    for s in range(2, sq):
        if n % s == 0:
            delll.append(s)
            delll2.append(n // s)
print(delll, delll2)





