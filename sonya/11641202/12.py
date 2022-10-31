for n in range(0, 10):
    s = '21'*n + '1'*(10-n)
    while '21' in s:
        s = s.replace('21', '5', 1)
    if s.count('1') + s.count('2')*2 + s.count('5')*5 == 34:
        print(n)