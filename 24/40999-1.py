file = open('40999.txt').read()
max_len = 0
data = file.split('A')
for i in data:
    if len(i) > max_len and i.count('E') >= 3:
        max_len = len(i)
print(max_len)
