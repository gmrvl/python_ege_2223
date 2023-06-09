from itertools import*
a = list(permutations('СПОРТЛОТО'))
count = 0
for x in a:
    s = ''.join(x)
    if 'ОО' in s:
        count += 1
print(count/(3*2*2))
