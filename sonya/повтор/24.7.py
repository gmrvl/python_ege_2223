file = open('24.7.txt')

ming = 1000000
for x in file:
    ming = min(ming, x.count('G'))
alth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = [0] * 26
file = open('24.7.txt')
for x in file:
    if x.count('G') == ming:
        for i in x:
            a[alth.find(i)] += 1
        break
maxx = max(a)
for i in range(26):
    if a[i] == maxx:
        print(alth[i])