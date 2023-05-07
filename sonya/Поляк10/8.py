from itertools import*
a = list(permutations('СПОРТЛОТО'))
d = set()
for x in a:
    s = ''.join(x)
    if s[0] != s[8]:
        d.add(s)
print(len(d))