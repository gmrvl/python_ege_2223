for n in range(1, 100):
    s = '1' + n * '0'
    while '10' in s or '1' in s:
        if '10' in s:
            s = s.replace('10', '001', 1)
        else:
            if '1' in s:
                s = s.replace('1', '0', 1)
    if len(s) == 3:
        print(n, s)