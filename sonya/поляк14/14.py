for x in '0123456789ABCDE':
    s = int('82' + x + '19', 15) - int('6' + x + '073',15)
    if s % 11 == 0:
        print( s //11)