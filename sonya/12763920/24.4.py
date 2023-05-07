file = open('24.4.txt')
minN = 10000000
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
        maxx = max(a)
        b = 0
        for i in range(26):
            if a[i] >= maxx:
                b = i
        print(alth[b])
        break



