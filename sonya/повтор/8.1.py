from itertools import*
a = product('0123456', repeat=4)
count = 0
for x in a:
    s = ''.join(x)
    if int(s[0]) > int(s[1]) > int(s[2]) > int(s[3]):
            count += 1
print(count)