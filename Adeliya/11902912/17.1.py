file = open('17.1.txt')
count = 0
k18 = [0]*45
n18 = [0]*45
max_k18 = [0]*45
min_k18 = [10000]*45
max_2 = [0]*45 # тут хранятся вторые максимумы. они могут быть кратными и не кратными 18, потому что нам ВСЕ РАВНО!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
maxpair = 0

for digit in file:
    digit = int(digit)
    ost45 = digit % 45
    if digit % 18 == 0:
        count += k18[ost45] + n18[ost45]
        k18[ost45] += 1

        if max_k18[ost45] < digit:
            # if max_2[ost45] < max_k18[ost45]:
            #     max_2[ost45] = max_k18[ost45]
            max_k18[ost45] = digit
        # elif max_2[ost45] < digit:
        #     max_2[ost45] = digit
        if min_k18[ost45] < digit:
            min_k18[ost45] = digit
    else:
        count += k18[ost45]
        n18[ost45] += 1

        # if max_2[ost45] < digit:
        #     max_2[ost45] = digit
    # if max_k18[ost45] != 0 and (abs(max_k18[ost45] - digit) > maxpair):
    #     maxpair = abs(max_k18[ost45] - digit)
    # elif min_k18 != 10000 and (abs(min_k18[ost45] - digit) > maxpair):
    #     maxpair = abs(min_k18[ost45] - digit)

# нужно создать такие массивы, чтобы ты хранила максимальные и минимальные числа для кратных 18 и не кратных 18

# for i in range(45):
#     if max_k18[i] != 0 and max_2[i] != 0:
#         d = abs(max_k18[i] - max_2[i])
#         if d > maxpair:
#             maxpair = d
print(count, maxpair)

