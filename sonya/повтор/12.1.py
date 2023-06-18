from itertools import*
a = product('12', repeat=14)
maxx = 0
for x in a:
    s = ''.join(x)
    if s.count('1') == 10 and s.count('2') == 4:
        while '11' in s:
            if '112' in s:
                s = s.replace('112', '6', 1)
            else:
                s = s.replace('11', '3', 1)
        c = 0
        for i in s:
            c += int(i)
        maxx = max(c, maxx)
print(maxx)