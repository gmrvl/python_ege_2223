file = open('35913.txt')

minNstring = file.readline()
minCountN = minNstring.count('N')

for string in file:
    if string.count('N') < minCountN:
        minNstring = string
        minCountN = string.count('N')

alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

maxS = 'A'
maxCount = minNstring.count('A')

for i in alp:
    if minNstring.count(i) >= maxCount:
        maxS = i
        maxCount = minNstring.count(i)
print(maxS)
