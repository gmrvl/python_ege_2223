a1 = []
for i in range(1, 1001):
    for j in range(1, 1001):
        x = i
        y = j
        if y > x:
            z = x
            x = y
            y = z
        a = x
        b = y
        while b > 0:
            r = a % b
            a = b
            b = r
        if a == 7 and x == 42:
            a1.append(y)
print(max(a1))
