file = open('24.2.txt')

alth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

max_dist = 0
for string in file:
    if string.count('G') < 25:
        for char in alth:
            dist = string.rfind(char) - string.find(char)
            if dist > max_dist:
                max_dist = dist
print(max_dist)
