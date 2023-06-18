for n in range(201,1000):
    s = '1' * n
    while '111' in s or '222' in s:
        s = s.replace('111', '22', 1)
        s = s.replace('222', '1', 1)
    if s.count('1') == 0:
        print(n)