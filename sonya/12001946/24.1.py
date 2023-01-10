file = open('24.1.txt').read()

len = 0
maxlen = 0
last = -1

for char in file:
    if last != -1:
        if char == 'P' and last == 'P':
            if len > maxlen:
                maxlen = len
            len = 1
        else:
            len += 1
    last = char
print(maxlen)