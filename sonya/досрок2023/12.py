for n in range(4,100):
    s = '3' + n * '5'
    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '3', 1)
        if '355' in s:
            s = s.replace('355', '52', 1)
        if '555' in s:
            s = s.replace('555', '23', 1)
    if (s.count('3') * 3 + s.count('2') * 2 + s.count('5') * 5) == 27:
        print(n)
        break