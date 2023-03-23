from itertools import*
a = list(product('012345678', repeat=5))

count = 0
ch = '02468'
for x in a:
    s = ''.join(x)
    if s[0] in ch:
        if s[4] != '1' and s[4] != '8':
            if s.count('3') <= 1:
                count += 1
print(count)