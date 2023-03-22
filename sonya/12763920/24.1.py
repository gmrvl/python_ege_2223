file = open('24.1.txt')
count = 0
maxcount = 0
for string in file:
    if string.count('A') < 25:
        for x in range(0, len(string) - 1):
            for y in range(x + 1, len(string)):
                if string[x] == string[y]:
                    count = abs(x - y)
                    maxcount = max(maxcount, count)
                    count = 0
print(maxcount)
