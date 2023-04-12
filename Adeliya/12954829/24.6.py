file=open('24.6.txt').read()
a = [0] * 26
alth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
last = ''

for i in file:
    if last == 'A':
        a[alth.find(i)] += 1
    last = i

for i in range(26):
    print(a[i], alth[i])
