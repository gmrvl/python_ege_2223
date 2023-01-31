count = 0
for i in range(1, 1001):
    n = bin(i)[2:]
    if i % 2 == 0:
        r = int('1' + n + '10', 2)
    else:
        r = int('11' + n + '0', 2)

    if 800 <= r <= 1500:
        print(n, r)
        count += 1
print(count)
