from itertools import*
a = list(product('АНТИУТОПИЯ', repeat=16))
count = 0
for x in a:
    s = ''.join(x)
    if s[0] != 'А' and s[-1] != 'Я':
        if 'АНТИУТОПИЯ' in s:
            count += 1
print(count)