file = open('r24.1.txt').read()
alth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = [0] * 26
last = ''

for char in file:
    if len(last) < 3:
        last += char
    if len(last) == 3:
        if last[0] == last[2]:
            a[alth.index(last[1])] += 1
        last = last[1:] + char
maxx = a.index(max(a))
print(alth[maxx])
