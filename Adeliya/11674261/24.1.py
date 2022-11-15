file = open('24.1.txt')

minNline = file.readline()
minCountN = minNline.count('N')

for line in file:
    count = line.count('N')
    if count < minCountN:
        minCountN = count
        minNline = line

alth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# charCounts = []
# for char in alth: - пригодится для рещения других задач
#     charCounts.append(minNline.count(char))
maxCount = 0
maxCountChar = ''
for char in alth:
    if minNline.count(char) >= maxCount:
        maxCount = minNline.count(char)
        maxCountChar = char
print(maxCountChar)

