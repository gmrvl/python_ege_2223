file = open('24.1.txt').read()
alth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = [0] * 26
last = ''
for i in file:
    if last == 'E':
        a[alth.find(i)] += 1
    last = i

print(alth[a.index(max(a))])
