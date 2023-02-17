file = open('r24.1.txt').read()
count = 0
string = ''

for char in file:
    if char == 'E':
        if len(string) == 0:
            string += char
        else:
            string += char
            if len(string) >= 12:
                count += 1
            string = char
    elif char == 'F':
        string = ''
    elif len(string) > 0:
        string += char
print(count)