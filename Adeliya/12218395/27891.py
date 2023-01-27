#  Х— наибольшим числом, кратным 14 и
#  являющимся произведением двух элементов последовательности с различными номерами.

file = open('27-B_2.txt')
s = file.readlines()
n = int(s[0])
# max14 * любое, max2 * max7
max14 = 0
max_14_2 = 0
max7 = 0
max2 = 0
max0 = 0
for i in s:
    i = int(i)
    if i == 50000:
        continue
    print(i)
    if i % 14 == 0:
        if i > max14:
            max_14_2 = max14
            max14 = i
        elif i > max_14_2:
            max_14_2 = i
    elif i % 7 == 0:
        if i > max7:
            max7 = i
    elif i % 2 == 0:
        if i > max2:
            max2 = i
    else:
        if i > max0:
            max0 = i

m = max(max2*max7, max14*max7, max14*max2, max14*max0, max14*max_14_2)
print(m)
