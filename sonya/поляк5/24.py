file = open('24-222.txt').read()
count = 0
maxcount = 0
last = ''
group = ''
c = 0

for char in file:
    if char == 'A':
        if last == 'A':
            count = 1
            continue
        elif last == group:
            count += len(group)
            print(last, group)
        else:
            maxcount = max(count + 1, maxcount)
            count = 1 + len(group)
        group = last
        last = char
    else:
        last += char
print(maxcount)
# for char in file:
#     if char == 'A':#         c += 1
#         if c == 1:
#             group = char
#         if c == 2:
#             count += len(group)
#         elif c > 2:
#             if group == last:
#                 count += len(group)
#             else:
#                 group = last
#                 if count + 1 > maxcount:
#                     maxcount = count + 1
#                 count = 1 + len(group)
#         count += 1
#         last = char
#     else:
#         if c == 1:
#             group += char
#         elif c > 1:
#             last += char

# for char in file:
#     if last == '' and char != 'A':
#         print('%', char)
#         continue
#     else:
#         print(char)
#         if char == 'A' and c == 0:
#             print('first A founded')
#             count += 1
#             c = 1
#         elif char == 'A':
#             flag = False
#             if group == last and group != '':
#                 count += len(group) + 1
#                 c += 1
#             else:
#                 c = 1
#                 group = last
#                 last = ''
#                 if count > maxcount:
#                     maxcount = count
#                 count = 1
#         elif not flag:
#             group += char
#         else:
#             print('*')
#             last += char
#
#
# print(maxcount)
