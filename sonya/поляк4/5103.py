rs = [0] * 1500
for n in range(0,  100000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '1' + str(r) + '10'
    else:
        r = '11' + str(r) + '0'
    r = int(r, 2)
    if 800 <= r <= 1500:
        rs[r] += 1

count = 0
for i in range(800, 1500):
    if rs[i] > 0:
        count += 1
print(count)

