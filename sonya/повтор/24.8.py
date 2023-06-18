file = open('24.8.txt')
rast = 0
for s in file:
    if s.count('A') < 25:
        for x in range(0, len(s)-1):
            for y in range(x + 1, len(s)):
                if s[x] == s[y]:
                    rast = max(rast, abs(x - y))
print(rast)