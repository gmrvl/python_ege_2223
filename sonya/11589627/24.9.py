file = open('24.9.txt').read()

count = 0
maxcount = 0
string = ''
maxstring = 0

for char in file:
    if char == 'A':
        string = ''
    else:
        string += char
        if string.count('E') >= 3 and len(string) > maxstring:
            maxstring = len(string)
if string.count('E') >= 3 and len(string) > maxstring:
    maxstring = len(string)
print(maxstring)















