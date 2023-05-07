file = open('47021.txt').read()
data = file.split('A')
count = 0
max_count = 0
for i in range(1, len(data) - 1):
    if data[i].count('B') == 0 and len(data[i]) >= 8:
        count += 1
print(count)
