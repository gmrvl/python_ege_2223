file = open('24.2.txt').read()

alth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

count = [0]*26
last = ''

for char in file:
    if len(last) < 3:
        last += char
    if len(last) == 3:
        if last[0] == last[2]:
            count[alth.find(last[1])] += 1
        last = last[1:] + char
print(count)
maxx = count.index(max(count))
print(alth[maxx])

