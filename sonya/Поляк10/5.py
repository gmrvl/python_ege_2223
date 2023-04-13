count = 0

for n in range(1,1000000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r + bin(r.count('1'))[2:]
    else:
        r = '1' + r + '00'
    r = int(r, 2)
    if 500 <= r <= 700:
        count += 1
print(count)