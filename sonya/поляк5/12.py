for n in range(40, 100):
    s = '>' + n*'21'
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1','22>',1)
        if '>2' in s:
            s = s.replace('>2','00>',1)
        if '>0' in s:
            s = s.replace('>0','11>',1)
    s = s.replace('>', '1', 1)
    if (s.count('1') + s.count('2') * 2) % 100 == 77:
        print(n)