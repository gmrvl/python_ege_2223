file = open('24.4.txt')
minN = 100000
for string in file:
    if string.count('N') < minN:
        minN = string.count('N')
alth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
file = open('24.4.txt')
for string in file:
    a = 26 * [0]
    if string.count('N') == minN:
        for char in string:
            a[alth.find(char)] += 1
        maxx = a.index(max(a))
        print(alth[maxx])



