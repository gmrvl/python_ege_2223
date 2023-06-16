a = '0123456789AB'
for x in a:
    s = int('28' + x + '2', 18) + int('93' + x + '5', 12)
    if s % 133 == 0:
        print(x)
        break