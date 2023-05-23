for i in range(1349341, 1949399942, 2023):
    s = str(i)
    if s[0] == '1' and s[2:5] == '493' and s[-2:] == '41':
        print(i)
