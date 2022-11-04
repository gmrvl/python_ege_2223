file = open('36879.txt')

alth = 'ABCDEFDHIJKLMNOPQRSTUVWXYZ'

max_r = 0
for string in file:
    if string.count('G') < 25:
        for char in alth:
            r = string.rfind(char) - string.find(char)
            if r > max_r:
                max_r = r

print(max_r)

