for i in range(123450708, 123459799):
    s = str(i)
    if s[0:5] == '12345' and s[6] == '7' and s[8] == '8':
        if i % 23 == 0:
            print(i, i//23)
