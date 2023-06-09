for k in range(100,201):
    for m in range(100, 201):
        for n in range(100, 201):
            s = '>' + k * '0' + m * '1' + n * '2'
            while '>1' in s or '>2' in s or '>0' in s:
                if '>1' in s:
                    s = s.replace('>1', '20>')
                if '>2' in s:
                    s = s.replace('>2 ', '00>')
                if '>0' in s:
                    s = s.replace('>0', '21>')
            summ = 0
            for i in range(0, len(s)):
                summ += int(s[i])
            if summ == 599:
                print(k)
