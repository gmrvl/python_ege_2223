from itertools import*
a = product('01234567', repeat=5)
count = 0
for x in a:
    s = ''.join(x)
    if s.count('6') == 1 and '60' not in s :
            count += 1
print(count)