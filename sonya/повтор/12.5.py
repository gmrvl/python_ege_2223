maxx = 0
for n in range(201,1000):
    s = '1' * n
    while '1111' in s:
        s = s.replace('1111', '22', 1)
        s = s.replace('222', '1', 1)
    maxx = max(s.count('1'), maxx)

for n in range(201,1000):
    s = '1' * n
    while '1111' in s:
        s = s.replace('1111', '22', 1)
        s = s.replace('222', '1', 1)
    if s.count('1') == maxx:
        print(n)