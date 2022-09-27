# def F(n, a):
#     if n == 0:
#         a.append(0)
#         return 0
#     elif n % 2 == 1:
#         a[n] = a[n - 1] + 1
#         return a[n]
#     else:
#         a[n] = a[n // 2]
#         return a[n]
#
#
# count = 0
# a = []
# for n in range(0, 1_000_001):
#     if F(n, a) == 3:
#         count += 1
#
# print(count)
