a = '55113'

for x in range(0,9):
    a = int(a, x)
    b = int('7' + str(x) + str(x) + '5', 80)
    if abs(a - b) < 1000000:
        print(x)
