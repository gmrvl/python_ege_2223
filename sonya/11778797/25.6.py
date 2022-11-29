# for i in range(10213904, 192139995):
#     if (i % 2023) == 0 and (i % 10) == 4 and (i // 100) % 10 == 9 and str(i)[0] == '1' and str(i)[2] == '2' and str(i)[3] == '1' and str(i)[4] == '3':
#         print(i, i // 2023)

for i in range(0, 10):
    string = '1' + str(i) + '21394'
    digit = int(string)
    if digit % 2023 == 0:
        print(digit, digit // 2023)

for i in range(0, 10):
    string = '1' + str(i) + '2139'
    for j in range(0, 1000):
        string2 = string + str(j) + '4'
        digit = int(string2)
        if digit % 2023 == 0:
            print(digit, digit // 2023)

