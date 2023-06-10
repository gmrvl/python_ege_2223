# for k in range(100, 201):
#     print('+')
#     for m in range(100, 201):
#         for n in range(100, 201):
#             s = '>' + k * '0' + m * '1' + n * '2'
#             while '>1' in s or '>2' in s or '>0' in s:
#                 if '>1' in s:
#                     s = s.replace('>1', '20>', 1)
#                 elif '>2' in s:
#                     s = s.replace('>2', '00>', 1)
#                 elif '>0' in s:
#                     s = s.replace('>0', '10>', 1)
#
#             if (s.count('1') + s.count('2')*2) == 599:
#                 print(k)

for k in range(100, 201):
    for m in range(100, 201):
        if k + 2*m == 599:  print(k)
