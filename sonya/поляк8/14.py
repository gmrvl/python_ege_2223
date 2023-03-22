for x in '0123456789ABCDEFGH':
    s = int('9009' + x, 18) + int('2257' + x,18)
    if s % 15 == 0:
        print(s //15)