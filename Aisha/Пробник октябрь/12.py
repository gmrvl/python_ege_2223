for i in range(1, 11):
    s = '21'*i + '1'*(10-i)
    while '21' in s:
        s = s.replace('21', '5', 1)

    if (s.count('1') + s.count('2')*2 + s.count('5')*5) == 34:
        print(i)
        break
