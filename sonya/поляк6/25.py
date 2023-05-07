for n in range(0,1000):
    s = int('1234' + str(n) + '7')
    if s % 141 == 0:
        print(s, s //141)