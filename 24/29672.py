# Определите количество строк, в которых буква E встречается чаще, чем буква A.

file = open('29672.txt')

count = 0
for string in file:
    if string.count('E') > string.count('A'):
        count += 1
print(count)
