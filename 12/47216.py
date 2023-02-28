for n in range(1, 1000):
    s = '>' + '0' * 39 + '1' * n + '2' * 39
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        elif '>2' in s:
            s = s.replace('>2', '2>', 1)
        else:
            s = s.replace('>0', '1>', 1)
    summ = s.count('1') + s.count('2') * 2
    prost = True
    for i in range(2, int(summ**0.5) + 1):
        if summ % i == 0:
            prost = False
            break
    if prost:
        print(n)
        break
