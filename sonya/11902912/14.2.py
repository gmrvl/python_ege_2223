

for x in range(1, 10):
    x = str(x)
    s = int('4C' + x + '4', 15) + int(x + '62A', 13)
    if s % 121 == 0:
        print(x, s // 121)