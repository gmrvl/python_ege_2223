for v in range(0, 10):
    for z in range(0, 10):
        s = int('12345' + str(v) + '7' + str(z) + '8')
        if s <= 10**9 and s % 23 == 0:
            print(s, s//23)