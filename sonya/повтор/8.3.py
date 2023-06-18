from itertools import*
a = permutations('ОЛЬГА')
count = 0
for x in a:
    s = ''.join(x)
    if s[0] != 'Ь' and 'ОЬ' not in s and 'АЬ' not in s:
        count += 1
print(count)