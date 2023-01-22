file = open('24.txt')

alth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
counts = [0] * 26

NS = 1000000
sstring = ''

for string in file:
    if 'N' in string:
        if string.count('N') < NS:
            NS = string.count('N')
            sstring = string

for i in range(0, len(sstring)):
    counts[alth.find(sstring[i])] += 1

maxx = max(counts)
for ii in range(0, len(counts)):
    if counts[ii] == maxx:
        print(alth[ii])


