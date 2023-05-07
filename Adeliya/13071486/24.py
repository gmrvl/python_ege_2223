file=open('24.txt')

minNstring = file.readline()
minCountN = minNstring.count('N')

for string in file:
    if string.count('N') < minCountN:
        minNstring = string
        minCountN = string.count('N')

alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

maxsim = 'A'
maxCount = minNstring.count('A')

for i in alph:
    if minNstring.count(i) >= maxCount:
        maxsim = i
        maxCount = minNstring.count(i)
print(maxsim)
