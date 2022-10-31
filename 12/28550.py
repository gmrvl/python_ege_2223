for i in range(1, 11):
    s = '21' * i + (10 - i) * '1'

    while '21' in s:
        s = s.replace('21', '5', 1)
    if (s.count('5') * 5 + s.count('2') * 2 + s.count('1')) == 34:
        print(i)
