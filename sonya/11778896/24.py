file = open('24.txt').read()

counts = [0]*26

alth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
last = ''

for char in file:
    if len(last) < 3:
        last += char
    if len(last) == 3:
        if last[0] == last[2]:
            counts[alth.find(last[1])] += 1
        last = last[2:] + char
maxx = counts.index(max(counts))
print(alth[maxx])
