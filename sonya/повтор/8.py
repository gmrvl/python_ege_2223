from itertools import*
a = product('0123', repeat=3)
count = 0
for x in a:
    s = ''.join(x)
    if (int(s[0]) + int(s[2])) > (int(s[1])):
        if s[0] != '0':
            count += 1
print(count)