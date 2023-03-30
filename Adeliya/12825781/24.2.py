file=open('24.2.txt')

alth = 'ABCDEFDHIJKLMNOPQRSTUVWXYZ'

maxx = 0
for string in file:
    if string.count('G') < 25:
        for i in alth:
            r = string.rfind(i) - string.find(i)
            if r > maxx:
                maxx = r

print(maxx)
