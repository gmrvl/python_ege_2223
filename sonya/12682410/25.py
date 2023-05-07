for v in '0123456789':
    for z in '0123456789':
        s = int('12345' + v + '7' + z + '8')
        if s % 23 == 0:
            print(s, s //23)