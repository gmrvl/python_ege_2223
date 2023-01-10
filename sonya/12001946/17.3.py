file = open('17.3.txt')

i = 0
s = 0
for string in file:
    string = int(string)
    if string % 2 == 0:
        i += string
        s += 1

srarifm = i//s

file = open('17.3.txt')
last = int(file.readline())
count = 0
maxsumm = 0

for sg in file:
    sg = int(sg)
    if ((sg % 3 == 0) or (last % 3 == 0)) and (sg < srarifm or last < srarifm):
        count += 1
        summ = sg + last
        if maxsumm < summ:
            maxsumm = summ
    last = sg

print(count,maxsumm)