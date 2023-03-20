for x in '01234567':
    for y in '01234567':
        s = int( y + '04' + x + '5', 11) + int('253' + x + y, 8)
        if s % 117 == 0:
            print(s // 117)
          