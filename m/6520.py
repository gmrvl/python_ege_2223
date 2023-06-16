for n in range(3, 101):
    s = '3' * 1 + '7' * n

    while '37' in s or '577' in s or '777' in s:
        if '37' in s:
            s = s.replace('37', '7', 1)
        elif '577' in s:
            s = s.replace('577', '73', 1)
        elif '777' in s:
            s = s.replace('777', '5', 1)
    if 9 < (s.count('7') * 7 + s.count('5') * 5 + s.count('3') * 3) < 100:
        print(n)