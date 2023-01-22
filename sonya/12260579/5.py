rs = []
for n in range(0, 1000):
    r = bin(n)[2:]
    if int(r) % 2 == 0:
        r = '1' + r + '0'
    elif n % 2 != 0:
        r = '11' + r + '11'
    r = int(r, 2)
    if r > 52:
        rs.append(r)
print(min(rs))