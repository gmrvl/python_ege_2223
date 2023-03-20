# дано число, заменить все 1 на 0, а все 0 на 1

n = 11000010010111
n = str(n)
new_str = ''
for i in range(len(n)):
    if n[i] == '1':
        new_str += '0'
    else:
        new_str += '1'

print(new_str)
