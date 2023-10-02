file = open('24.6.txt').read()
last = ''
alth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = [0] * 26
for char in file:
    if len(last) < 3:
        last += char
    else:
        if last[0] == last[2]:
            a[alth.find(last[1])] += 1
        last = last[1:] + char
maxx = max(a)
for i in range(26):
    if a[i] == maxx:
        print(alth[i])