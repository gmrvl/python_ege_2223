file = open('24.txt')
alth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = 26*[0]
mincountN = 10000000
for string in file:
    countN = string.count('N')
    mincountN = min(mincountN, countN)

file = open('24.txt')
for string in file:
    if string.count('N') == mincountN:
        for i in string:
            a[alth.find(i)] += 1
        maxx = max(a)
        for j in range(26):
            if a[j] == maxx:
                print(alth[j])
        break
