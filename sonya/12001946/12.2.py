for n in range(10):
    for m in range(10):
        for p in range(10):
            s = '0' + '1' * n + '2' * m + '3' * p + '0'
            b = '0' + '1' * n + '2' * m + '3' * p + '0'
            while not '00' in s:
                s.replace('01', '210', 1)
                s.replace('02', '320', 1)
                s.replace('03', '3012', 1)
            if s.count('1') == 25 and s.count('2') == 54 and s.count('3') == 48:
                print(len(b))