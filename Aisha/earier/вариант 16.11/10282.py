for i in range(10000, 100000):
    n = str(i)
    nechet = int(n[0]) + int(n[2]) + int(n[4])
    chet = int(n[1]) + int(n[3])
    if nechet > chet:
        result = str(chet) + str(nechet)
    else:
        result = str(nechet) + str(chet)
    if result == '723':
        print(i)
        break
