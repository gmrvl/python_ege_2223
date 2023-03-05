file = open('24-215.txt')
count = 0
maxcount = 0
last = ''
strr = file.readline()
strr = strr.replace('1', '*')
strr = strr.replace('2', '*')
strr = strr.replace('3', '*')
strr = strr.replace('A', '#')
strr = strr.replace('B', '#')
strr = strr.replace('C', '#')

strr = strr.replace('*#*', '1')

for i in strr:
    if i == '1':
        count += 1
    else:
        maxcount = max(maxcount, count)
        count = 0

# for char in file:
#     if len(last) < 3:
#         last += char
#     if len(last) == 3:
#         if last[0] == ('1' or '2' or '3') and last[2] == ('1' or '2' or '3') and last[1] == ('A' or 'B' or 'C'):
#             count += 1
#             last = ''
#         else:
#             maxcount = max(maxcount, count)
#             count = 0
#             last = last[1:]
print(maxcount)