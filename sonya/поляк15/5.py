a = []
for n in range(1,10000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '1' + r + '10'
    else:
        r = '11' + r + '0'
    r = int(r,2)
    if 800 <= r <= 1500:
        if r not in a:
            a.append(r)
print(len(a))