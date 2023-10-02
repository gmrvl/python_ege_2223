for n in range(0,100):
    s = '>' + 39 * '0' + n * '1' + 39 * '2'
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)
    summ = s.count('1') + s.count('2') * 2
    sq = int(summ**0.5)
    dells = 0
    for dell in range(1, sq + 1):
        if summ % dell == 0:
            dells += 2
            if dells > 2:
                break
    if dells == 2:
        print(n)