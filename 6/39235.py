c = 0
for i in range(10001):
    s = i
    s = 3 * (s // 10)
    n = 1
    while s < 221:
        s = s + 13
        n = n * 2
    if n == 256:
        c = c + 1
print(c)