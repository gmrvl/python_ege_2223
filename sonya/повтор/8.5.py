from itertools import*
a = permutations('РУСЛАН')
count = 0
for x in a:
    s = ''.join(x)
    if 'УА' not in s and 'АУ' not in s:
        count += 1
print(count)