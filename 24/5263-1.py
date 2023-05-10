words = ["ABEC", "BDAC", "CAFB", "CFBA"]
with open('5263.txt') as file:
    line = file.readline()
i, count, ans = 0, 0, 0
prev = ''
while i + 4 < len(line):
    sub_line = line[i: i + 4]
    if sub_line in words and (prev == '' or prev[3] == sub_line[0]):
        count += 1
        prev = sub_line
        i += 3
    else:
        ans = max(ans, count)
        count = 0
        prev = ''
        i += 1
ans = max(ans, count)
print(ans)
