from itertools import*
a = product('НИКОЛАЙ', repeat=4)
count = 0
for x in a:
    s = ''.join(x)
    if s[0] != 'Й' and ('О' in s or 'А' in s or 'И' in s):
            count += 1
print(count)