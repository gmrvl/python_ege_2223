
for i in range(10213904, 192139995):
    if (i % 2023) == 0 and (i % 10) == 4 and (i // 100) % 10 == 9 and str(i)[0] == '1' and str(i)[2] == '2' and str(i)[3] == '1' and str(i)[4] == '3':
        print(i, i // 2023)
