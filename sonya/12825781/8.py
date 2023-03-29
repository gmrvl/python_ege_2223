from itertools import*
a = list(product('андрей', repeat=6))


count = 0
for x in a:
    s = ''.join(x)
    flag = True
    if (s.count('й') > 1) or s[0] == 'й' or s[5] == 'й' or 'ей' in s or 'йе' in s:
        flag = False
    if flag:
        count += 1
print(count)