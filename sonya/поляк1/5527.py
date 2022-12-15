#задание17

file = open('17-345.txt')
min = 10000
max = 0

for string in file:
    string = int(string)
    if string % 100 == 52:
        if string > max:
            max = string
        if string < min:
            min = string

raz = max - min

counts = 0
maxsumm = 0
last = 0
file = open('17-345.txt')

for s in file:
    s = int(s)
    if last >= 1:
        if (last < raz and s >= raz) or (last >= raz and s < raz):
            counts += 1
            summ = s + last
            if maxsumm < summ:
                maxsumm = summ
    last = s
print(raz, counts,maxsumm)