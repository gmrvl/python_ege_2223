for x in '0123456789ABC':
    s = int('8' + x + '121', 13) - int('7' + x + '575', 13)
    if s % 19 == 0:
        print(s//19)