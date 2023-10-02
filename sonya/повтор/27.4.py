file = open('4-27989_B.txt')
N = int(file.readline())
del26 = 0
del13 = 0
del2 = 0
for i in file:
    i = int(i)
    if i % 26 == 0:
        del26 += 1
    elif i % 13 == 0:
        del13 += 1
    elif i % 2 == 0:
        del2 += 1
print(del2*del13+ del26 * (N - del26)+ (del26 * (del26 - 1)/2))