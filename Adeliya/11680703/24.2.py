file=open('24.2.txt')
alth = 'ABCDEFDHIJKLMNOPQRSTUVWXYZ'

max = 0
for s in file:
    if s.count('G') < 25:
        for i in alth:
            r = s.rfind(i) - s.find(i)
            if r > max:
                max = r
print(max)