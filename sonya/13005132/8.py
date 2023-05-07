from itertools import*
a = list(product('012345678', repeat=7))
count = 0
for x in a:
    s = ''.join(x)
    if s[0] != '0':
        if s.count('6') == 1:
            if s.count('1') + s.count('3') + s.count('5') + s.count('7') == 2:
                count += 1
print(count)
