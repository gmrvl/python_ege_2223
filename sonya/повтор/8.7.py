from itertools import*
a = product('АНДРЕЙ', repeat=6)
count = 0
for x in a:
    s = ''.join(x)
    if s[0] != 'Й' and s[-1] != 'Й' and 'ЕЙ' not in s and 'ЙЕ' not in s and s.count('Й') <= 1:
        count += 1
print(count)