file = open('35913.txt')
minNstr = 'N'*1000000000
for s in file:
    if s.count('N') < minNstr.count('N'):
        minNstr = s
alth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
maxLetter = ''
count = 0
for i in alth:
    if minNstr.count(i) >= count:
        count = minNstr.count(i)
        maxLetter = i
print(maxLetter)
