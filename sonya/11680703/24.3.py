file = open('24.3.txt').read()

stringcount = 0
string = ''

for char in file:
    if char == 'E' and len(string) == 0:
        string += char
    elif char == 'E' and len(string) > 0:
        string += char
        if len(string) >= 12:
            stringcount += 1
        string = char
    elif char == 'F':
        string = ''
    elif len(string) > 0:
        string += char
print(stringcount)