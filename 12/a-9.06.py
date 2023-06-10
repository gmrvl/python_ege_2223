for n in range(4, 1000):
    s = '3' + '5'*n
    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '3', 1)
        elif '355' in s:
            s = s.replace('355', '52', 1)
        elif '555' in s:
            s = s.replace('555', '23', 1)
    summ = s.count('2')*2 + s.count('5')*5 + s.count('3')*3
    if summ == 27:
        print(n)
        break
