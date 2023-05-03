for a in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    r = int('Z' + a + 'YX', 55) - int('2X' + a + 'Y', 55)
    if r % 29:
        print(r)