a = '55113'

for x in range(6, 10):
    a = int('55113', x)
    b = 7 * (80**3) + x * (80**2) + x * (80**1) + 5 * (80**0)
    print(a, b)

    if abs(a - b) < 1000000:
        print(x)
