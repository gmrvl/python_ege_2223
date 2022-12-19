for n in range(3, 1000, 3):
    c = n // 3
    s = '3'*c + '2'*c + '1'*c
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
            break
