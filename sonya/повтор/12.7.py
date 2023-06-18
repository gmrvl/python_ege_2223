for n in range(6,100):
    s = '21' * 5 + 5 * '1' + '2' * (n - 5)
    while '21' in s:
        s = s.replace('21', '5', 1)
    if s.count('1') + s.count('2')*2 + s.count('5')* 5 == 34:
        print(n)