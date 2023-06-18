file = open('24.txt')
alth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
minG = 10000000
for string in file:
    if string.count('G') < minG:
        minG = string.count('G')
file = open('24.txt')
for string in file:
    a = 26 * [0]
    if string.count('G') == minG:
        for char in string:
            a[alth.find(char)] += 1
        maxx = max(a)
        b = 0
        for i in range(26):
            if a[i] == maxx:
                b = i
        print(alth[b])
        break