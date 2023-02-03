for k in range(200, 100, -1):
    for m in range(200, 100, -1):
        for n in range(200, 100, -1):
            s = '>' + k * '1' + m * '2' + n * '*'
            while '>1' in s or '>2' in s or '>*' in s:
                if '>1' in s:
                    s = s.replace('>1', '111>', 1)
                if '>2' in s:
                    s = s.replace('>2', '1>', 1)
                if '>*' in s:
                    s = s.replace('>*', '%2*>', 1)

            if s.count('1') + s.count('2')*2 == 1190:
                print(n)


