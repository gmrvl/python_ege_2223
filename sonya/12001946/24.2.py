file = open('24.2.txt').read()

alth = 'ABCDEFJHIGKLMNOPQRSTUVWXYZ'
counts = [0]*26
last = ''

for char in file:
    if last == 'A':
        counts[alth.index(char)] += 1
    last = char
maxx = counts.index(max(counts))
print(alth[maxx])