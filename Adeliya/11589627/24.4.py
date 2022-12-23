file = open('24.4.txt').read()
count = [0]*26

alth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
last = ''
for i in file:
    if last == 'A':
        counts[alth.find(i)] += 1
    last = i
maxx = counts.index(max(counts))

print(alth[maxx])
