def ДЕЛ(n, m):
    if n % m == 0:
        return 1
    else:
        return 0
b = []
for i in range(70,81):
    b.append(i)
set(b)
countA = 0
for A in range(1,1000):
    ok = True
    for x in range(1,1000):
        if (ДЕЛ(x, 12) and (x in b) and (not(ДЕЛ(x, A)))) == 1:
            ok = False
            break
    if ok:
        countA += 1
print(countA)
