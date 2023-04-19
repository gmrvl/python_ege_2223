from itertools import*
a = permutations('СПОРТЛОТО')
count = 0
for x in a:
    s = ''.join(x)
    if 'ТТ' in s:
        count += 1
print(count)