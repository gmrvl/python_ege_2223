for n in range(1000):
    s = '3'*n + '2'*n + '1'*n
    while '21' in s or '31' in s or '32' in s:
        if '21' in s:
            s = s.replace('21', '12', 1)
        if '31' in s:
            s = s.replace('31', '13', 1)
        if '32' in s:
            s = s.replace('32', '23', 1)
    if len(s) >= 50:
        if s[49] == '2':
            print(n)
