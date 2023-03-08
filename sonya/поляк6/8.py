from itertools import*
a = list(product('видео', repeat=6))

count = 0
for x in a:
    s = ''.join(x)
    if 'и' in s and 'е' in s:
        t = list(s)
        t = [x for x in t if (x in 'иео')]
        if t == sorted(t):
            count += 1
print(count)