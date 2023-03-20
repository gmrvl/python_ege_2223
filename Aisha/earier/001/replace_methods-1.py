# дано число, заменить все 1 на 0, а все 0 на 1

n = 11000010010111
n = str(n)

n = n.replace('1', 'k')
n = n.replace('0', '1')
n = n.replace('k', '0')

print(n)
