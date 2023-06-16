for i in range(3023, 10**10, 3023):
    s = str(i)
    if s[0] == '1' and s[2:5] == '954' and s[-2:] == '27':
        print(i)
