from itertools import*
a = list(permutations('матвей'))
count = 0
for x in a:
    s = ''.join(x)
    if s[0] != 'й':
        if not 'ае' in s:
            count += 1
print(count)