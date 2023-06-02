from itertools import *
a = list(product('АНТИУОПЯ', repeat=16))
count = 0

for x in a:
    s = ''.join(x)
    if 'АНТИУТОПИЯ' in s:
        count += 1
print(count)
