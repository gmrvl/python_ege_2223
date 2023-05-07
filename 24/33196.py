file = open('33196.txt').read()

counts = [0] * 26
alth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
last = ''

for i in file:
    if last == 'A':
        counts[alth.find(i)] += 1
    last = i

for i in range(26):
    print(counts[i], alth[i])
