file = open('35482.txt')
minGline = str(file.readline)
minCountG = minGline.count('G')
for line in file:
    c = line.count('G')
    if c < minCountG:
        minCountG = c
        minGline = str(line)

for i in 'abcd':
    if minGline.count(i) > maxCo:
        maxCo = minGline.count(i)
