for i in range(2023, 10**10, 2023):
    i = str(i)
    if i[0] == '1' and i[2:6] == '2139' and i[-1] == '4':
        i = int(i)
        print(i, i // 2023)