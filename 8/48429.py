count = 0
for i in range(9 ** 6, 9 ** 7):
    res = ''
    while i != 0:
        res += str(i % 9)
        i //= 9
    if res.count('6') == 1 and (res.count('1') + res.count('3') + res.count('5') + res.count('7')) == 2:
        count += 1
print(count)
