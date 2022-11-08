file = open('24.....txt').read()

counts = [0]*26
alth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
last = ''

for char in file:
    if last == 'A':
        counts[alth.index(char)] += 1
    last = char
maxx = counts.index(max(counts))
print(alth[maxx])