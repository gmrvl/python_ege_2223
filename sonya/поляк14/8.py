from itertools import *
a = list(permutations('СПОРТЛОТО'))
count = 0
for x in a:
    s = ''.join(x)
    if 'ООО' in s:
        count += 1
print(count/12)