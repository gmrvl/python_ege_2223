from itertools import*
a = permutations('СВЕТЛАНА')
count = 0
for x in a:
    s = ''.join(x)
    if 'АА' not in s:
        count += 1
print(count/2)