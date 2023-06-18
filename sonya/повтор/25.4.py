a = []
for n in range(1,100,2):
    for m in range(0,100,2):
        if 200000000 <= (2**m) * (3**n) <= 400000000:
            a.append((2**m) * (3**n))
print(sorted(a))