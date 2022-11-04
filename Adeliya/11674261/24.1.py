file=open('24.1.txt')
minNline = str(file.readline)
minCountN = minNline.count('N')
for line in file:
    c = line.count('N')
    if c < minCountN:
        minCountN = c
        minNline = str(line)


