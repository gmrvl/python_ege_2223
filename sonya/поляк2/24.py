file = open('24-230.txt').read()


chislo = ''
c = 0
chisla = []

for char in file:
    if c == 0 and char == 'Z':
        chislo += char
        c = 1
    if c == 1 and char == '8':
        chislo += char
        c = 2
    if c == 2 and (char == '0' or char == '1' or char == '3' or char == '3' or char == '4' or char == '5'or char == '6' or char == '7' or char == '8' or char == '9'):
        chislo += char
        c = 3
    if c == 3 and (char == '0' or char == '1' or char == '3' or char == '3' or char == '4' or char == '5'or char == '6' or char == '7' or char == '8' or char == '9'):
        chislo += char
        c = 4
    if c == 4 and (char == '0' or char == '1' or char == '3' or char == '3' or char == '4' or char == '5'or char == '6' or char == '7' or char == '8' or char == '9'):
        chislo += char
        c = 5
    if c == 5 and char == '5':
        chislo += char
        c = 6
    if c == 6 and char == '4':
        chislo += char
        c = 7
    if c == 7 and (char == '0' or char == '1' or char == '3' or char == '3' or char == '4' or char == '5'or char == '6' or char == '7' or char == '8' or char == '9'):
        chislo += char
        c = 8
    if c == 8 and (char == '0' or char == '1' or char == '3' or char == '3' or char == '4' or char == '5'or char == '6' or char == '7' or char == '8' or char == '9'):
        chislo += char
        c = 9
    if c == 9 and (char == '0' or char == '1' or char == '3' or char == '3' or char == '4' or char == '5'or char == '6' or char == '7' or char == '8' or char == '9'):
        chislo += char
        c = 10
    if c == 10 and char == '2':
        chislo += char
        c = 11
    if c == 11 and char == '2':
        chislo += char
        c = 12
    if c == 12 and char == 'Z':
        chislo += char
        chislo = chislo[1:]
        chislo = chislo[:-1]
        chislo = int(chislo)
        chisla.append(chislo)
        chislo = ''
        c = 0
    else:
        c = 0
        chislo = ''
print(max(chisla))

