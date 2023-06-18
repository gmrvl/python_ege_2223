file = open('24.5.txt').read()
alth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = [0] * 26
last = ''
for char in file:
    if last == 'A':
        a[alth.find(char)] += 1
    last = char
maxx = max(a)
for i in range(26):
    if a[i] == maxx:
        print(alth[i])