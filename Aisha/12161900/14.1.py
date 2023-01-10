for x in '01234567':
    for y in '01234567':
        s = int(x + '01' + y + '4', 9) + int(x + y + '544', 8)
        if s % 89 == 0:
           print(s // 89)
           break
