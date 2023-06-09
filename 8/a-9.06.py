count = 0
for i in range(100, 1000):
    d = ''
    while i != 0:
        d = str(i % 5) + d
        i //= 5
    a = list(map(int, list(d)))
    flag = True
    for digit in range(len(a) - 1):
        if a[digit] <= a[digit + 1]:
            flag = False
            break
    if flag:
        count += 1
        print(d, int(d, 5))
print(count)
