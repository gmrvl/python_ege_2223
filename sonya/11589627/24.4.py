file = open('24.4.txt').read()
counts = [0]*26 # массив, в котором храним инфу сколько раз буква встретилась сразу за "А"

alth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
last = ''
for char in file:
    if last == 'A':
        counts[alth.find(char)] += 1
    last = char
maxx = counts.index(max(counts))

print(alth[maxx])


