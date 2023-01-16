file = open('17.3.txt')
count = 0
maxx = 0
maxPair = 0
arr = [int(i) for i in file]
for i in arr:
    k = i ** 2
    if k > maxx and (i % 10 == 3):
        maxx = i ** 2
# for i in range(len(arr) - 1):
#     for j in range(i + 1, len(arr)):
#         summ = i ** 2 + j ** 2
#         if (summ > maxx) and (((i % 10 == 3) and (j % 10 != 3)) or ((i % 10 != 3) and (j % 10 == 3))):
#             count += 1
#             if summ > maxPair:
#                 maxPair = summ
print(count, maxPair)
