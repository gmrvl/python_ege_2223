file = open('24.11.txt').read()

groups = 0
string = ''

for char in file:
    if char == 'E' and len(string) == 0:
        string += char
    elif char == 'E' and len(string) > 0:
        string += char
        if len(string) >= 12:
            groups += 1
        string = char
    elif char == 'F':
        string = ''
    elif len(string) > 0:
        string += char
print(groups)

