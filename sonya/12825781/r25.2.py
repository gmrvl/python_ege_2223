ns = []
chet = []
nchet = []
for i in range(100):
    if i % 2 == 0:
        chet.append(i)
    else:
        nchet.append(i)
for n in nchet:
    for m in chet:
        if 200000000 <= (2 ** m) * (3 ** n) <= 400000000:
            ns.append((2 ** m) * (3 ** n))
print(sorted(ns))