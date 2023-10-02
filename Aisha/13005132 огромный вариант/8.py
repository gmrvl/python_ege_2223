count = 0
for i in range(9 ** 6, 9 ** 7):
    s = ''
    while i != 0:
        s = str(i % 9) + s
        i //= 9
    if s.count('6') == 1 and (s.count('1') + s.count('3') + s.count('5') + s.count('7')) == 2:
        count += 1
print(count)

