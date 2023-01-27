# Необходимо определить количество пар, для которых произведение элементов кратно 62

c62 = 0
c2 = 0
c31 = 0
total = 0
c0 = 0

file = open('27990_B.txt')

count = 0
i = int(file.readline())

for n in file:
    n = int(n)
    if n % 62 == 0:
        count += total
        c62 += 1
    elif n % 2 == 0:
        count += (c31 + c62)
        c2 += 1
    elif n % 31 == 0:
        count += (c2 + c62)
        c31 += 1
    else:
        c0 += 0
        count += c62
    total += 1

print(count, total)

# f = open("27990_B.txt")  # для файла A укажите его название
# s = f.readlines()
# n = int(s[0])
# k_0 = 0
# k_62 = 0
# k_2 = 0
# k_31 = 0
# for i in range(1, n + 1):
#     s[i] = int(s[i])
#     if s[i] % 62 == 0:
#         k_62 += 1
#     elif s[i] % 31 == 0:
#         k_31 += 1
#     elif s[i] % 2 == 0:
#         k_2 += 1
#     else:
#         k_0 += 1
# k = k_62 * k_0 + k_31 * k_2 + k_62 * k_31 + k_62 * k_2 + (k_62 * (k_62 - 1)) // 2
# print(k)
