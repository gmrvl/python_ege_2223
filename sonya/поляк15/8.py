from itertools import*
a = list(permutations('КОМПЬЮТЕР'))
count = 0
for x in a:
    s = ''.join(x)
    if s[8] == 'Е' and s[0]<s[1]<s[2]<s[3]:
        count += 1
print(count)