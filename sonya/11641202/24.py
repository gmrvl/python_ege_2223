file = open('24....txt').read()

c = 0
string = 0
stringcount = 0


for char in file:
    if char == 'E':
        if c == 1:
            string += 1
            if string >= 12:
                stringcount += 1
            string = 1
        else:
            c = 0
            string += 1
        c += 1
    elif char == 'F':
        string = 0
        с = 0
    else:
        if c == 1:
            string += 1
print(stringcount)