s = 350 - 1

a = ''
while s > 0:
    n = str(s % 4)
    a = n + a
    s //= 4
a = str(a)
a = a.replace('0','А')
a = a.replace('1','К')
a = a.replace('2','Р')
a = a.replace('3','У')
print(a)