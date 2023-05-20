file = open('38958.txt').read()
a = []
maxx = 0
count = 0
for char in file:
    if char != 'D':
        count += 1
    else:
        maxx = max(maxx, count)
        count = 0
maxx = max(maxx, count)

print(count, maxx)
