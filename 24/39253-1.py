file = open('38958.txt').read()
max_len = 0
data = file.split('D')
for i in range(len(data) - 1):
    if len(data[i + 1] + data[i]) > max_len:
        max_len = len(data[i + 1] + data[i]) + 1
print(max_len)
