from itertools import*
a = permutations('СПОРТЛОТО')
count = 0
for x in a:
    s = ''.join(x)
    if s[0] != 'О' and s[-1] != 'О':
        count += 1
print(count//12)#збавляемся от повторов делением на 2! и 3!
