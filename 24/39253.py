file = open('38958.txt').read()
max_len = 0
data = file.split('D')
for i in range(0, len(data) - 1):
    if len(data[i]) + len(data[i + 1]) + 1 > max_len:
        max_len = len(data[i]) + len(data[i + 1]) + 1

print(max_len)
