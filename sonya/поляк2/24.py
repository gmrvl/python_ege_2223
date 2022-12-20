file = open('24-230.txt').read()


chislo = ''

for char in file:
    if chislo == '':
        if char == 'Z':
            chislo += char
    if chislo[0] == 'Z' and len(chislo) == 1:
        if char == '8':
            chislo += '8'
    if chislo[0] == 'Z' and chislo[1] == '8' and len(chislo) == 2:
        if char == '0' or char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' or char == '7' or char == '8' or char == '9':
            chislo += char
    if chislo[0] == 'Z' and chislo[1] == '8' and len(chislo) == 3:
        if char == '0' or char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' or char == '7' or char == '8' or char == '9':
            chislo += char
    if chislo[0] == 'Z' and chislo[1] == '8' and len(chislo) == 4:
        if char == '0' or char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' or char == '7' or char == '8' or char == '9':
            chislo += char
    if chislo[0] == 'Z' and chislo[1] == '8' and len(chislo) == 5 :
        if char == '5':
            chislo += char
    if chislo[0] == 'Z' and chislo[1] == '8' and len(chislo) == 6 and chislo[6] == '5' :
        if char == '4':
            chislo += char
    if chislo[0] == 'Z' and chislo[1] == '8' and len(chislo) == 7 and chislo[6] == '5' and chislo[7] == '4':
        if char == '0' or char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' or char == '7' or char == '8' or char == '9':
            chislo += char
    if chislo[0] == 'Z' and chislo[1] == '8' and len(chislo) == 7 and chislo[6] == '5' and chislo[7] == '4':
        if char == '0' or char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' or char == '7' or char == '8' or char == '9':
            chislo += char
