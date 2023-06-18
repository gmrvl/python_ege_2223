file = open('27686.txt').read()
count = 0
max_count = 0

for char in file:
    if char == 'Z':
        count += 1
    else:
        max_count = max(count, max_count)
        count = 0

print(max_count)