from itertools import*
a = permutations('ЛЕВИЙ')
count = 0
for x in a:
    s = ''.join(x)
    if s[0] != 'Й' and 'ЕИ' not in s:
        count += 1
print(count)
