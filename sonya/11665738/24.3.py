file = open('24.3.txt').read()

counts = [0]*26
alth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
last = ''

for char in file:
    if len(last) < 3:
        last += char
    else:
        if last[1] == last[2]:
            counts[alth.find(char)] += 1
        last = last[1:] + char
maxx = counts.index(max(counts))
print(counts)
print(alth[maxx])
