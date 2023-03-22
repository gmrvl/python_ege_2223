file = open('24.2.txt').read()
alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = 26 * [0]
last = ''
for char in file:
    if last == 'E':
        a[alf.index(char)] += 1
    last = char
maxx = a.index(max(a))
print(alf[maxx])