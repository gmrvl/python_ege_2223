for x in '0123456789A':
    s = int('3364' + x, 11) + int(x + '7946', 12)
    b = int('55' + x + '87', 14)
    if s == b:
        print(b)