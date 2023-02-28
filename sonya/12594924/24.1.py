file = open('24.1.txt').read()
alth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = [0] * 26
last = ''
for char in file:
    if last == 'E':
        a[alth.index(char)] += 1
    last = char
maxx = a.index(max(a))
print(alth[maxx])