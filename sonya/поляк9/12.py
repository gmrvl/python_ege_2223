for n in range(251, 1000):
    s = '5' * n
    while '55555' in s:
        s = s.replace('55555', '88', 1)
        s = s.replace('888', '555', 1)
    if s.count('5') == 1:
        print(n)