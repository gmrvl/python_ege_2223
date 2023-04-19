count = 0
for n in range(2,100000):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = '1' + r + '11'
    else:
        r = '11' + r + '0'
    r = int(r,2)
    if 500 <= r <= 1000:
        count += 1
print(count)

