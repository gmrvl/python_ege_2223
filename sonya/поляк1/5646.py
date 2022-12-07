#задание24

file = open('24-230.txt').read()
'43??78???34'
string = ''
maxstring = 0

for char in file:
    if len(string) < 13:
        string += char
    if len(string) == 13:
        if string[0] == 'K' and string[1] == '4' and string[2] == '3' and string[5] == '7' and string[6] == '8' and string[10] == '3' and string[11] == '4' and string[12] == 'K':
            s = string[1] + string[2] + string[3] + string[4] + string[5] + string[6] + string[7] + string[8] + string[9] + string[10] + string[11]
            s = int(s)
            if s > maxstring:
                maxstring = s
        string = string[1:] + char
print(maxstring)

#?
maxstring = str(maxstring)
proizveden = 0
for s in range(0, 10):
    if proizveden == 0:
        if int(maxstring[s]) % 2 != 0:
            proizveden += int(maxstring[s])
    if proizveden > 0:
        if int(maxstring[s]) % 2 != 0:
            proizveden *= int(maxstring[s])
print(proizveden)