for x in '0123456789ABCDEFG':
    s = int('66' + x + '63', 17) - int('5' + x + '810', 17)
    if s % 11 == 0:
        print(s // 11)