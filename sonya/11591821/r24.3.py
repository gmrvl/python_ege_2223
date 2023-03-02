file = open('r24.3.txt')
maxrast= 0
for string in file:
    if string.count('A') < 25:
        for x in range(0, len(string) - 1):
            for y in range(x + 1, len(string)):
                if string[x] == string[y]:
                    rast = abs(x - y)
                    maxrast = max(maxrast, rast)
print(maxrast)