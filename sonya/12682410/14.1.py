for x in '0123456789A':
    s = int('95' + x + '2', 11) + int(x + '458', 12)
    if s % 136 == 0:
        print(s //136)