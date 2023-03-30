file = open('24.2.txt')
alth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rast = 0
maxrast = 0
for string in file:
    if string.count('G') < 25:
        for x in range(0, len(string) - 1):
            for y in range(x + 1, len(string)):
                if string[x] == string[y]:
                    rast = abs(y - x)
                    maxrast = max(maxrast, rast)
print(maxrast)